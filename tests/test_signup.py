from src.app import activities


def test_signup_success_adds_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "test.user@example.com"
    assert email not in activities[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert resp.json()["message"] == f"Signed up {email} for {activity}"
    assert email in activities[activity]["participants"]


def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Activity"
    email = "noone@example.com"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Activity not found"


def test_signup_already_signed_up_returns_400(client):
    # Arrange
    activity = "Chess Club"
    # use an existing participant from the initial dataset
    existing = activities[activity]["participants"][0]

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": existing})

    # Assert
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Student already signed up for this activity"
