import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    """PokeAPI Settings"""

    database_url: str = "sqlite://:memory:"  # Default is a sqlite in memory
    database_models: list = ["api.database.schemas"]
    app_mode: str = "Development"

    class Config:
        case_sensitive: bool = True
        env_file = os.path.expanduser(".env")
