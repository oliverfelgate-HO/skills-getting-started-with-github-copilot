def test_signup_for_activity_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"
    signup_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(signup_path, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Signed up {email} for {activity_name}"
    }


def test_signup_for_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    signup_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(signup_path, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_duplicate_student_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"
    signup_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(signup_path, params={"email": existing_email})

    # Assert
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Student already signed up for this activity"
    }


def test_signup_without_email_returns_422(client):
    # Arrange
    activity_name = "Chess Club"
    signup_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(signup_path)

    # Assert
    assert response.status_code == 422
