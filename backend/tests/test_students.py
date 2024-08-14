import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)



@pytest.fixture
def test_student(entity_path):
    return "test_student_id"

@pytest.fixture
def entity_path():
    return "/api/student/"

# Test creating a student

def test_create_student(test_student,entity_path):
    response = client.post(entity_path, json={
        "_key": test_student,
        "first_name": "John",
        "last_name": "Doe",
        "dob": "2005-04-23",
        "rank": "green_belt",
        "contact_info": {"email": "johndoe@example.com"}
    })
    assert response.json()["_key"] == test_student

# Test retrieving a student
def test_get_student(test_student,entity_path):
    response = client.get(f"{entity_path}{test_student}")
    assert response.status_code == 200
    assert response.json()["first_name"] == "John"

# Test updating a student
def test_update_student(test_student,entity_path):
    response = client.put(f"{entity_path}{test_student}", json={
        "_key": test_student,
        "first_name": "Johnny",
        "last_name": "Doe",
        "dob": "2005-04-23",
        "rank": "green_belt",
        "contact_info": {"email": "johnnydoe@example.com"}
    })
    assert response.status_code == 200
    assert response.json()["first_name"] == "Johnny"

# Test deleting a student
def test_delete_student(test_student,entity_path):
    response = client.delete(f"{entity_path}{test_student}")
    assert response.status_code == 200
    assert response.json()["message"] == "student entity deleted successfully"
