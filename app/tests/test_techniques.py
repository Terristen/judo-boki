import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture
def test_id(test_collection_path):
    return "test_technique_id"

@pytest.fixture
def test_collection_path():
    return "/api/technique/"


#create a record
def test_create(test_id,test_collection_path):
    response = client.post(test_collection_path, json={
        "_key": test_id,
        "name": "Test Record",
        "description": "Test Description",
        "translation": "Test Translation"
    })
    assert response.json()["_key"] == test_id

# Test retrieving a record
def test_get(test_id,test_collection_path):
    response = client.get(f"{test_collection_path}{test_id}")
    assert response.status_code == 200
    assert response.json()["_key"] == test_id

# Test updating a record
def test_update(test_id,test_collection_path):
    response = client.put(f"{test_collection_path}{test_id}", json={
        "_key": test_id,
        "name": "Test Record",
        "description": "Test Description",
        "translation": "Test Translation",
        "new_field": "New Field"
    })
    assert response.status_code == 200
    assert "new_field" in response.json()

# Test deleting a record
def test_delete(test_id,test_collection_path):
    response = client.delete(f"{test_collection_path}{test_id}")
    assert response.status_code == 200
    assert "entity deleted successfully" in response.json()["message"]
