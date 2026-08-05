from src.app import activities


def test_remove_participant_success(client):
    # Arrange
    activity = "Basketball Team"
    email = "alex@mergington.edu"
    assert email in activities[activity]["participants"]

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert resp.json()["message"] == f"Removed {email} from {activity}"
    assert email not in activities[activity]["participants"]


def test_remove_participant_activity_not_found_404(client):
    # Arrange
    activity = "No Such"
    email = "ghost@example.com"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Activity not found"


def test_remove_participant_not_found_404(client):
    # Arrange
    activity = "Basketball Team"
    email = "not-in-list@example.com"
    assert email not in activities[activity]["participants"]

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Participant not found"
