import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

@pytest.fixture
def test_tag_data():
    return {
        "_from": "students/student_12345",
        "_to": "sessions/session_67890",
        "relationship": "attended",
        "notes": "Test attendance"
    }

@pytest.fixture
def test_tag_path():
    return "/tag/attended/"

## These do not work yet because you need edges to link to otherwise you get a 404

# def test_create_tag(test_tag_path, test_tag_data):
#     response = client.post(test_tag_path, json=test_tag_data)
#     assert response.status_code == 200
#     assert response.json()["message"] == "Tag created"
#     assert "key" in response.json()

# def test_get_tag(test_tag_data):
#     response = client.get(f"/tags/{test_tag_data['_from']}")
#     assert response.status_code == 200
#     assert len(response.json()["result"]) > 0
#     assert response.json()["result"][0]["link"]["relationship"] == test_tag_data["relationship"]

# def test_update_tag(test_tag_data):
#     updated_data = {
#         "notes": "Updated attendance notes"
#     }
#     response = client.put(f"/tag/?_from={test_tag_data['_from']}&_to={test_tag_data['_to']}&relationship={test_tag_data['relationship']}", json=updated_data)
#     assert response.status_code == 200
#     assert response.json()["updated_tag"]["notes"] == "Updated attendance notes"

# def test_delete_tag(test_tag_data):
#     response = client.delete(f"/tag/?_from={test_tag_data['_from']}&_to={test_tag_data['_to']}&relationship={test_tag_data['relationship']}")
#     assert response.status_code == 200
#     assert response.json()["message"] == "Tag removed successfully"

# def test_batch_add_tags():
#     batch_data = [
#         {
#             "_from": "students/student_12345",
#             "_to": "sessions/session_67890",
#             "relationship": "attended",
#             "notes": "Batch attendance 1"
#         },
#         {
#             "_from": "students/student_12345",
#             "_to": "sessions/session_67891",
#             "relationship": "attended",
#             "notes": "Batch attendance 2"
#         }
#     ]
#     response = client.post("/tags/batch", json=batch_data)
#     assert response.status_code == 200
#     assert len(response.json()["results"]) == 2
