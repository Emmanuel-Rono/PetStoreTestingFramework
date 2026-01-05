# Configuration/config.py
import os
from Configuration.settings import DEFAULT_HEADERS, DEFAULT_TIMEOUT
from Configuration.environments import ENVIRONMENTS

class Config:
    def __init__(self):
        self.env = os.getenv("ENV", "qa")
        if self.env not in ENVIRONMENTS:
            raise ValueError(f"Unknown environment: {self.env}")
        self.base_url = ENVIRONMENTS[self.env]["base_url"]
        self.headers = DEFAULT_HEADERS
        self.timeout = DEFAULT_TIMEOUT
config = Config()

