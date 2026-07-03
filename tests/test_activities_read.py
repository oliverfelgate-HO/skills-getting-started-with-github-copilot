def test_get_activities_returns_seeded_data(client):
    # Arrange
    activities_path = "/activities"

    # Act
    response = client.get(activities_path)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]
    assert isinstance(data["Chess Club"]["participants"], list)
