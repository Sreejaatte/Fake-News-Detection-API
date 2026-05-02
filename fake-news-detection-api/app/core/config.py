from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "Fake News Detection API"
    ENV: str = "development"
    HOST: str = "0.0.0.0"
    PORT: int = 10000

    MODEL_PATH: str = "app/models/fake_news_model.pkl"
    VECTORIZER_PATH: str = "app/models/vectorizer.pkl"

    LOG_LEVEL: str = "INFO"
    LOG_JSON: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
