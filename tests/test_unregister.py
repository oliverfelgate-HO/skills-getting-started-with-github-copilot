def test_unregister_from_activity_success(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"
    unregister_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.delete(unregister_path, params={"email": existing_email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {existing_email} from {activity_name}"
    }


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    unregister_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.delete(unregister_path, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_student_not_signed_up_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    missing_email = "not.enrolled@mergington.edu"
    unregister_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.delete(unregister_path, params={"email": missing_email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Student is not signed up for this activity"
    }


def test_unregister_without_email_returns_422(client):
    # Arrange
    activity_name = "Chess Club"
    unregister_path = f"/activities/{activity_name}/signup"

    # Act
    response = client.delete(unregister_path)

    # Assert
    assert response.status_code == 422
