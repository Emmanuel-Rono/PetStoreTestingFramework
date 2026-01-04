import pytest

from Tests.conftest import pet_service


def test_create_pet(pet_service):
    create_pet_response = pet_service.add_pet()
    assert create_pet_response.status_code == 201

    response_body = create_pet_response.json()
    assert response_body.get("id") == ["id"]

