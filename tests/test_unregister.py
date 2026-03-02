from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_unregister_participant():
    # Arrange: sign up a user first
    activities = client.get("/activities").json()
    activity_name = next(iter(activities.keys()))
    email = "unregisteruser@mergington.edu"
    client.post(f"/activities/{activity_name}/signup?email={email}")
    # Act: unregister
    response = client.post(f"/activities/{activity_name}/unregister?email={email}")
    # Assert: check response
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    # Act: try to unregister again (should fail)
    response2 = client.post(f"/activities/{activity_name}/unregister?email={email}")
    # Assert: should not allow unregistering non-existent
    assert response2.status_code != 200 or "not found" in response2.text.lower()
