from fastapi import APIRouter, HTTPException, Body, Query
from backend.routes.common_crud import get_entity, upsert_entity, delete_entity, get_all_entities

router = APIRouter()

# Specify the collection name for the entity
collection_name = "classification"

@router.get(f"/{collection_name}")
def get_entities():
    return get_all_entities(collection_name)

@router.get(f"/{collection_name}/{{entity_id}}")
def get_specific_entity(entity_id: str):
    return get_entity(collection_name, entity_id)

@router.post(f"/{collection_name}/")
def create_specific_entity(entity_data: dict = Body(...)):
    return upsert_entity(collection_name, entity_data)

@router.put(f"/{collection_name}/{{entity_id}}")
def update_specific_entity(entity_id: str, entity_data: dict = Body(...)):
    return upsert_entity(collection_name, entity_data, entity_id)

@router.delete(f"/{collection_name}/{{entity_id}}")
def delete_specific_entity(entity_id: str):
    return delete_entity(collection_name, entity_id)
