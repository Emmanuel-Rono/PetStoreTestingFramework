import pytest
from Configuration.config import config
from Data.pet_payload import pet_payload_factory
from Services import PetService

@pytest.fixture(scope="session")
def app_config():
    return config

@pytest.fixture(scope="session")
def pet_service(app_config):
    return PetService(
        base_url=app_config.base_url,
        headers=app_config.headers,
        timeout=app_config.timeout
    )

@pytest.fixture
def valid_pet_payload():
    """Provides a valid pet payload."""
    return pet_payload_factory()

@pytest.fixture
def sold_pet_payload():
    """Provides a valid pet payload with status 'sold'."""
    return pet_payload_factory(status="sold")

@pytest.fixture
def created_pet(pet_service, valid_pet_payload):
    """Creates and cleans up a pet resource."""
    create_response= pet_service.add_pet(valid_pet_payload)
    pet_data = create_response.json()
    pet_id = pet_data["id"]

    yield pet_data
    try:
        pet_service.delete_pet(pet_id)
    except Exception:
        pass



