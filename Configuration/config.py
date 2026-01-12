# Configuration/config.py
from Configuration.settings import DEFAULT_HEADERS, DEFAULT_TIMEOUT
from Configuration.environments import ENVIRONMENTS

class Config:
    def __init__(self, env="qa"):
        if env not in ENVIRONMENTS:
            raise ValueError(f"Unknown environment: {env}")
        self.env = env
        self.base_url = ENVIRONMENTS[env]["base_url"]
        self.headers = DEFAULT_HEADERS
        self.timeout = DEFAULT_TIMEOUT
