# Conf/config.py
import os
from Conf.settings import DEFAULT_HEADERS, DEFAULT_TIMEOUT
from Conf.environments import ENVIRONMENTS

class Config:
    def __init__(self):
        self.env = os.getenv("ENV", "qa")
        if self.env not in ENVIRONMENTS:
            raise ValueError(f"Unknown environment: {self.env}")
        self.base_url = ENVIRONMENTS[self.env]["base_url"]
        self.headers = DEFAULT_HEADERS
        self.timeout = DEFAULT_TIMEOUT
config = Config()
