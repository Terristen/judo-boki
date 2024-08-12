from fastapi import APIRouter, HTTPException, Body, Query
from arango.collection import Collection
from config import db

router = APIRouter()

# Upsert function
def upsert_tag(collection: Collection, tag_data: dict):
    # Check if the relationship already exists
    query = """
        FOR doc IN @@collection
        FILTER doc._from == @from AND doc._to == @to AND doc.relationship == @relationship
        RETURN doc._key
    """
    cursor = db.aql.execute(query, bind_vars={
        "@collection": collection.name,
        "from": tag_data["_from"],
        "to": tag_data["_to"],
        "relationship": tag_data["relationship"]
    })
    existing_key = next(cursor, None)

    if existing_key:
        # Update the existing edge
        collection.update_match({"_key": existing_key}, tag_data)
        return {"message": "Tag updated", "key": existing_key}
    else:
        # Insert new edge
        new_edge = collection.insert(tag_data)
        return {"message": "Tag created", "key": new_edge["_key"]}


# Common delete function for removing tags
@router.delete("/tag/")
def remove_tag(
    from_id: str = Query(..., alias="_from"),
    to_id: str = Query(..., alias="_to"),
    relationship: str = Query(...),
):
    collection_name = f"tag_{relationship}"
    
    # Check if the collection exists
    if not db.has_collection(collection_name):
        raise HTTPException(status_code=404, detail=f"Collection {collection_name} not found")

    collection = db.collection(collection_name)

    # Build AQL query to find the specific edge
    query = """
        FOR doc IN @@collection
        FILTER doc._from == @from AND doc._to == @to AND doc.relationship == @relationship
        REMOVE doc IN @@collection
        RETURN OLD
    """
    cursor = db.aql.execute(query, bind_vars={
        "@collection": collection_name,
        "from": from_id,
        "to": to_id,
        "relationship": relationship
    })
    
    result = next(cursor, None)
    
    if result:
        return {"message": "Tag removed successfully", "removed": result}
    else:
        raise HTTPException(status_code=404, detail="Tag not found")

# Example usage:
# DELETE /tag/?_from=students/student_12345&_to=sessions/session_67890&relationship=attended


# Common GET function for retrieving tags using graph traversal
@router.get("/tag/")
def get_tags(
    entity_id: str = Query(...), 
    relationship: str = Query(...),
    direction: str = Query(..., pattern="^(out|in)$")  # Must be "out" or "in"
):
    # Determine the direction for the graph traversal
    if direction == "out":
        direction_option = "OUTBOUND"
    else:
        direction_option = "INBOUND"

    # Correct the traversal query syntax
    query = f"""
        FOR v, e, p IN 1..1 {direction_option} @entity_id GRAPH 'FullSchema'
        FILTER e.relationship == @relationship
        RETURN {{ vertex: v, edge: e }}
    """
    
    # Execute the query
    cursor = db.aql.execute(query, bind_vars={
        "entity_id": entity_id,
        "relationship": relationship
    })

    # Transform the results to the desired format
    results = [{"record": doc["vertex"], "link": doc["edge"]} for doc in cursor]

    if results:
        return {"result": results}
    else:
        raise HTTPException(status_code=404, detail="No matching tags found")

# Example usage:
# GET /tag/?entity_id=sessions/session_67890&relationship=is_sub_of&direction=out
# or
# GET /tag/?entity_id=sessions/session_67890&relationship=attended&direction=in


# Helper function to check collection existence
def get_collection(relationship: str):
    collection_name = f"tag_{relationship}"
    if not db.has_collection(collection_name):
        raise HTTPException(status_code=404, detail=f"Collection {collection_name} not found")
    return db.collection(collection_name)


## Routes
@router.post("/tag/is_in/")
def add_tag_is_in(
    from_id: str = Body(..., alias="_from"),
    to_id: str = Body(..., alias="_to"),
    relationship: str = Body("is_in"),
    notes: str = Body(None)
):
    collection = get_collection(relationship)
    
    tag_data = {
        "_from": from_id,
        "_to": to_id,
        "relationship": relationship,
        "notes": notes
    }

    return upsert_tag(collection, tag_data)

@router.post("/tag/achieved/")
def add_tag_achieved(
    from_id: str = Body(..., alias="_from"),
    to_id: str = Body(..., alias="_to"),
    relationship: str = Body("achieved"),
    date_of_test: str = Body(None),
    test_score: int = Body(None),
    tester: str = Body(None)
):
    collection = get_collection(relationship)

    tag_data = {
        "_from": from_id,
        "_to": to_id,
        "relationship": relationship,
        "date_of_test": date_of_test,
        "test_score": test_score,
        "tester": tester
    }

    return upsert_tag(collection, tag_data)

@router.post("/tag/is_sub_of/")
def add_tag_is_sub_of(
    from_id: str = Body(..., alias="_from"),
    to_id: str = Body(..., alias="_to"),
    relationship: str = Body("is_sub_of")
):
    collection = get_collection(relationship)

    tag_data = {
        "_from": from_id,
        "_to": to_id,
        "relationship": relationship
    }

    return upsert_tag(collection, tag_data)

@router.post("/tag/covered/")
def add_tag_covered(
    from_id: str = Body(..., alias="_from"),
    to_id: str = Body(..., alias="_to"),
    relationship: str = Body("covered")
):
    collection = get_collection(relationship)

    tag_data = {
        "_from": from_id,
        "_to": to_id,
        "relationship": relationship
    }

    return upsert_tag(collection, tag_data)

@router.post("/tag/requires/")
def add_tag_requires(
    from_id: str = Body(..., alias="_from"),
    to_id: str = Body(..., alias="_to"),
    relationship: str = Body("requires")
):
    collection = get_collection(relationship)

    tag_data = {
        "_from": from_id,
        "_to": to_id,
        "relationship": relationship
    }

    return upsert_tag(collection, tag_data)

@router.post("/tag/attended/")
def add_tag_attended(
    from_id: str = Body(..., alias="_from"),
    to_id: str = Body(..., alias="_to"),
    relationship: str = Body("attended")
):
    collection = get_collection(relationship)

    tag_data = {
        "_from": from_id,
        "_to": to_id,
        "relationship": relationship
    }

    return upsert_tag(collection, tag_data)


##Utility functions

@router.put("/tag/")
def update_tag(
    from_id: str = Query(..., alias="_from"),
    to_id: str = Query(..., alias="_to"),
    relationship: str = Query(...),
    updated_data: dict = Body(...)
):
    collection_name = f"tag_{relationship}"

    if not db.has_collection(collection_name):
        raise HTTPException(status_code=404, detail=f"Collection {collection_name} not found")

    collection = db.collection(collection_name)

    # Find the edge
    query = """
        FOR doc IN @@collection
        FILTER doc._from == @from AND doc._to == @to AND doc.relationship == @relationship
        RETURN doc
    """
    cursor = db.aql.execute(query, bind_vars={
        "@collection": collection_name,
        "from": from_id,
        "to": to_id,
        "relationship": relationship
    })
    existing_tag = next(cursor, None)

    if existing_tag:
        # Update the edge with new data
        updated_tag = {**existing_tag, **updated_data}
        collection.update_match({"_key": existing_tag["_key"]}, updated_tag)
        return {"message": "Tag updated successfully", "updated_tag": updated_tag}
    else:
        raise HTTPException(status_code=404, detail="Tag not found")


@router.get("/tags/{entity_id}")
def list_all_tags_for_entity(entity_id: str):
    query = """
        FOR v, e, p IN 1..1 ANY @entity_id GRAPH 'FullSchema'
        RETURN {vertex: v, edge: e}
    """
    
    cursor = db.aql.execute(query, bind_vars={"entity_id": entity_id})
    
    results = [{"record": doc["vertex"], "link": doc["edge"]} for doc in cursor]

    if results:
        return {"result": results}
    else:
        raise HTTPException(status_code=404, detail="No tags found for this entity")


@router.post("/tags/batch")
def batch_add_tags(tags: list[dict]):
    results = []
    for tag in tags:
        collection_name = f"tag_{tag['relationship']}"
        if not db.has_collection(collection_name):
            raise HTTPException(status_code=404, detail=f"Collection {collection_name} not found")

        collection = db.collection(collection_name)
        
        # Perform the upsert for each tag
        upsert_result = upsert_tag(collection, tag)
        results.append(upsert_result)
    
    return {"results": results}


@router.get("/tag/{key}")
def get_tag_by_key(key: str, relationship: str = Query(...)):
    collection_name = f"tag_{relationship}"
    if not db.has_collection(collection_name):
        raise HTTPException(status_code=404, detail=f"Collection {collection_name} not found")

    collection = db.collection(collection_name)
    tag = collection.get(key)
    
    if tag:
        return {"tag": tag}
    else:
        raise HTTPException(status_code=404, detail="Tag not found")

@router.get("/tags/count/")
def count_tags(
    entity_id: str = Query(...),
    relationship: str = Query(...),
    direction: str = Query(..., pattern="^(out|in)$")
):
    if direction == "out":
        direction_option = "OUTBOUND"
    else:
        direction_option = "INBOUND"

    query = f"""
        RETURN LENGTH(
            FOR v, e, p IN 1..1 {direction_option} @entity_id GRAPH 'FullSchema'
            FILTER e.relationship == @relationship
            RETURN e
        )
    """
    
    count = db.aql.execute(query, bind_vars={
        "entity_id": entity_id,
        "relationship": relationship
    }).next()

    return {"count": count}

@router.delete("/tags/{entity_id}/clear")
def clear_all_tags_for_entity(entity_id: str):
    query = """
        FOR v, e, p IN 1..1 ANY @entity_id GRAPH 'FullSchema'
        REMOVE e IN @@edge_collection
    """
    
    # Assumes edge collections are named consistently, otherwise iterate over possible collections
    collections = ["tag_is_in", "tag_is_sub_of", "tag_attended", "tag_requires", "tag_achieved"]
    results = []
    
    for collection_name in collections:
        cursor = db.aql.execute(query, bind_vars={
            "entity_id": entity_id,
            "@edge_collection": collection_name
        })
        results.extend(list(cursor))
    
    if results:
        return {"message": "Tags removed successfully", "removed": len(results)}
    else:
        raise HTTPException(status_code=404, detail="No tags found for this entity")


## nage waza = classification/7903
## koshi waza = classification/7941
## ashi waza = classification/7978
## te waza = classification/7995