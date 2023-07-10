import os
from pydantic import BaseSettings
from pathlib import Path
from superagi.lib.logger import logger

class Config(BaseSettings):
    class Config:
        env_file_encoding = "utf-8"
        extra = "allow"  # Allow extra fields

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_config(self, key: str, default: str = None) -> str:
        return getattr(self, key, default)

ROOT_DIR = os.path.dirname(Path(__file__).parent.parent)
_config_instance = Config()

def get_config(key: str, default: str = None) -> str:
    return _config_instance.get_config(key, default)
