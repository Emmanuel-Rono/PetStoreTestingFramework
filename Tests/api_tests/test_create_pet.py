import pytest

from Tests.conftest import pet_service, valid_pet_payload


def test_create_pet(pet_service,valid_pet_payload):
    create_pet_response = pet_service.add_pet(valid_pet_payload)
    assert create_pet_response.status_code == 200

    response_body = create_pet_response.json()
    assert response_body.get("id") == valid_pet_payload["id"]
    assert response_body.get("name") == valid_pet_payload["name"]
    assert response_body.get("description") == valid_pet_payload["description"]

