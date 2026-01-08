def test_update_pet_with_form_data(pet_service,created_pet):
    pet_id=created_pet["id"]

    #Update pet logic
    response = pet_service.update_pet_form(
        pet_id=pet_id,
        name="newName",
        status="pending"
    )

    #assert Http

    assert response.status_code == 200

    #Verify changes were made
    response_to_check_if_pet_updated =pet_service.get_pet_by_id(pet_id)
    assert  response_to_check_if_pet_updated.status_code == 200

    #Verify the updated pet now
    new_pet_data = response_to_check_if_pet_updated.json()
    assert new_pet_data["name"] == "newName"
    assert new_pet_data["status"] == "pending"
