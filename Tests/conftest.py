# Tests/conftest.py
import pytest
from Configuration.config import Config
from Data.pet_payload import pet_payload_factory
from Services.pet_service import PetService

#addoption for env access via cmd
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against (dev, qa, prod)"
    )

@pytest.fixture(scope="session")
def app_config(request):
    """
    Returns a Config object initialized for the target environment.
    Environment is passed via CLI using --env
    """
    env = request.config.getoption("--env")
    return Config(env=env)

@pytest.fixture(scope="session")
def pet_service(app_config):
    """
    Returns a PetService instance using the selected environment configuration.
    """
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
    """
    Creates a pet resource before the test and cleans it up after the test.
    """
    create_response = pet_service.add_pet(valid_pet_payload)
    pet_data = create_response.json()
    pet_id = pet_data["id"]

    yield pet_data
    try:
        pet_service.delete_pet(pet_id)
    except Exception:
        pass
