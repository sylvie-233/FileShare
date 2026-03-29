from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FileShare"
    VERSION: str = "0.1.0"
    API_V1_PREFIX: str = "/api/v1"
    
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    UPLOAD_DIR: Path = Path("uploads")
    MAX_FILE_SIZE: int = 100 * 1024 * 1024
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
settings.UPLOAD_DIR.mkdir(exist_ok=True)
