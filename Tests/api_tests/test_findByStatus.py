import pytest

from Tests.conftest import pet_service

@pytest.mark.regression
def test_find_by_status(pet_service, sold_pet_payload):
    create_sold_pet_response = pet_service.add_pet(sold_pet_payload)
    assert create_sold_pet_response.status_code == 200

    #Find now by status
    response = pet_service.find_pet_by_status("sold")
    assert response.status_code == 200

    response_body = response.json()
    assert  isinstance(response_body,list)
    assert  len(response_body) > 0

    #Checking if status is actually marked sold
    for pet in response_body:
        assert pet["status"] =="sold"
