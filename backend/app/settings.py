from pydantic_settings import BaseSettings
from functools import lru_cache
from pydantic import Field
from typing import Optional

class SettingsCore(BaseSettings):
    DEBUG: bool = False
    APP_NAME: str = "Horoshop"

class PostgresSettings(BaseSettings):
    PGHOST: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: int = 5432

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }

    def DATABASE_ASYNC_URL(self) -> str:
        return (f"postgresql+asyncpg://{self.PGUSER}:{self.PGPASSWORD}@"
                f"{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}")

class Settings(SettingsCore, PostgresSettings):
    pass

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()