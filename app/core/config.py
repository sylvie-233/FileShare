from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

from app.core.paths import get_exe_dir


class Settings(BaseSettings):
    PROJECT_NAME: str = "FileShare"
    VERSION: str = "0.1.0"
    API_V1_PREFIX: str = "/api/v1"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    UPLOAD_DIR: Path = Path("uploads")
    MAX_FILE_SIZE: int = 100 * 1024 * 1024

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.UPLOAD_DIR.is_absolute():
            self.UPLOAD_DIR = get_exe_dir() / self.UPLOAD_DIR

    model_config = ConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()
settings.UPLOAD_DIR.mkdir(exist_ok=True)
