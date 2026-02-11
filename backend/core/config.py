from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "NexaAI"
    ENV: str = "development"
    DATABASE_URL: str = "sqlite:///./nexaai.db"
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
