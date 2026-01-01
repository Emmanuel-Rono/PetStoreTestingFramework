import pytest
from Conf import config
from Services.pet_service import PetService

@pytest.fixture(scope="session")
def app_config():
    """
    Provides read-only access to application settings.
    """
    return config

@pytest.fixture(scope="session")
def pet_service(app_config):
    """
    Session-scoped Pet API service.
    """
    return PetService(
        base_url=app_config.base_url,
        headers=app_config.headers,
        timeout=app_config.timeout
    )

@pytest.fixture
def created_pet(pet_service, valid_pet_payload):

    # Create
    create_response = pet_service.add_pet(valid_pet_payload)
    pet_data = create_response.json()

    pet_id = pet_data["id"]

    yield pet_data

    # Cleanup
    pet_service.delete_pet(pet_id)
