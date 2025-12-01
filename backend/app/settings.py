from pydantic_settings import BaseSettings
from functools import lru_cache



class SettingsCore(BaseSettings):
    DEBUG: bool = False
    APP_NAME: str = "Horoshop"

class Settings(SettingsCore):
    pass

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()