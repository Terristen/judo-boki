from fastapi import HTTPException
from config import db
import uuid

def get_entity(collection_name: str, entity_id: str):
    collection = db.collection(collection_name)
    entity = collection.get(entity_id)
    if entity:
        return entity
    else:
        raise HTTPException(status_code=404, detail=f"{collection_name} entity not found")

def get_all_entities(collection_name: str):
    """
    Returns all entities from the specified collection.
    """
    try:
        collection = db.collection(collection_name)
        cursor = collection.all()
        entities = [entity for entity in cursor]
        return entities
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def upsert_entity(collection_name: str, entity_data: dict, entity_id: str = None):
    """
    Upserts or inserts an entity in the specified collection based on the rules provided.
    """
    try:
        # Ensure entity_id is set correctly
        if entity_id is None:
            if "_key" in entity_data:
                entity_id = entity_data["_key"]
            else:
                entity_id = str(uuid.uuid4())
        else:
            entity_data["_key"] = entity_id

        # Prepare AQL parts for insert and update
        insert_fields = ", ".join([f"{k}: @insert_{k}" for k in entity_data])
        update_fields = ", ".join([f"{k}: @update_{k}" for k in entity_data if k != "_key"])

        query = f"""
        UPSERT {{ _key: @key }}
        INSERT {{ _key: @key, {insert_fields} }}
        UPDATE {{ {update_fields} }}
        IN {collection_name}
        RETURN NEW
        """
        
        # Prepare bind variables for AQL query
        bind_vars = {
            "key": entity_id
        }
        
        # Add bind variables for insert
        for k, v in entity_data.items():
            bind_vars[f"insert_{k}"] = v
        # Add bind variables for update (excluding _key)
        for k, v in entity_data.items():
            if k != "_key":
                bind_vars[f"update_{k}"] = v

        
        # Execute the AQL query
        cursor = db.aql.execute(query, bind_vars=bind_vars)
        result = cursor.next()

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error upserting {collection_name} entity: {str(e)}")
    
    
def create_entity(collection_name: str, entity_data: dict):
    collection = db.collection(collection_name)
    try:
        entity = collection.insert(entity_data)
        return entity
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating {collection_name} entity: {str(e)}")

def update_entity(collection_name: str, entity_data: dict, entity_id: str):
    collection = db.collection(collection_name)
    entity = collection.get(entity_id)
    if entity:
        updated_entity = {**entity, **entity_data}
        collection.update_match({"_key": entity["_key"]}, updated_entity)
        return updated_entity
    else:
        raise HTTPException(status_code=404, detail=f"{collection_name} entity not found")

def delete_entity(collection_name: str, entity_id: str):
    collection = db.collection(collection_name)
    entity = collection.get(entity_id)
    if entity:
        collection.delete(entity)
        return {"message": f"{collection_name} entity deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"{collection_name} entity not found")


## alternative implementation of delete_entity using AQL
# def delete_entity(collection_name: str, entity_id: str):
#     # Construct the AQL query to delete the entity
#     aql_query = f"""
#     FOR entity IN {collection_name}
#         FILTER entity._key == @entity_id
#         REMOVE entity IN {collection_name}
#         RETURN OLD
#     """
    
#     # Execute the AQL query
#     bind_vars = {"entity_id": entity_id}
#     cursor = db.aql.execute(aql_query, bind_vars=bind_vars)
    
#     # Check if the entity was deleted
#     deleted_entity = list(cursor)
#     if deleted_entity:
#         return {"message": f"{collection_name} entity deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail=f"{collection_name} entity not found")