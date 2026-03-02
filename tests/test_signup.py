from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_signup_for_activity():
    # Arrange: get an activity name
    activities = client.get("/activities").json()
    activity_name = next(iter(activities.keys()))
    email = "testuser@mergington.edu"
    # Act: sign up
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert: check response
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    # Act: try to sign up again (should fail or be handled)
    response2 = client.post(f"/activities/{activity_name}/signup?email={email}")
    # Assert: should not allow duplicate
    assert response2.status_code != 200 or "already" in response2.text.lower()
