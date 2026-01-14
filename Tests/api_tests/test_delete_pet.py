import pytest

@pytest.mark.regression
def test_delete_pet(pet_service, created_pet):
    pet_id = created_pet["id"]

    # Act: delete the pet
    delete_response = pet_service.delete_pet(pet_id)

    # Assert delete response
    assert delete_response.status_code == 200

    # Assert pet no longer exists
    get_response = pet_service.get_pet_by_id(pet_id)
    assert get_response.status_code == 404
