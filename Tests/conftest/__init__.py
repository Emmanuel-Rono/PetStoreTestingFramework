import pytest
from Conf import config


@pytest.fixture(scope="session")
def app_config():
    """
    Provides read-only access to application settings.
    """
    return config
