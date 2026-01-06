def test_update_pet(pet_service, created_pet):
    # Arrange: modify existing pet
    updated_payload = created_pet.copy()
    updated_payload["name"] = "Updated-Doggie"
    updated_payload["status"] = "sold"

    # Act
    response = pet_service.update_pet(updated_payload)

    # Assert HTTP
    assert response.status_code == 200

    response_body = response.json()

    # Assert identity
    assert response_body["id"] == created_pet["id"]

    # Assert updates
    assert response_body["name"] == "Updated-Doggie"
    assert response_body["status"] == "sold"
