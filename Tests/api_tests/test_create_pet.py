import pytest
from unicodedata import category

from Tests.conftest import pet_service, valid_pet_payload


def test_create_pet(pet_service,valid_pet_payload):
    create_pet_response = pet_service.add_pet(valid_pet_payload)
    assert create_pet_response.status_code == 200

    response_body = create_pet_response.json()
    assert response_body.get("id") == valid_pet_payload["id"]
    assert response_body.get("name") == valid_pet_payload["name"]
    assert response_body.get("photoUrls") == valid_pet_payload["photoUrls"]
    assert response_body.get("tags") == valid_pet_payload["tags"]

    assert "tags" in response_body
    assert isinstance(response_body["tags"], list)
    assert response_body["tags"][0]["id"] == valid_pet_payload["tags"][0]["id"]
    assert response_body["tags"][0]["name"] == valid_pet_payload["tags"][0]["name"]

    #Assertions for Category
    assert "category" in response_body
    assert response_body["category"]["id"] == valid_pet_payload["category"]["id"]
    assert response_body["category"]["name"] == valid_pet_payload["category"]["name"]