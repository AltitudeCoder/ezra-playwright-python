from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Config:
    base_url = "https://myezra-staging.ezra.com"

config = Config()

