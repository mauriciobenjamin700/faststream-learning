from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        str_strip_whitespace=True,
        case_sensitive=True,
        extra="ignore",
    )

    # Application
    APP_NAME: str = "FastStream Learning"
    APP_VERSION: str = "0.1.0"

    # Server
    DB_URL: str = "sqlite+aiosqlite:///./test.db"
    DB_ECHO: bool = False

    BROKER_URL: str = "amqp://guest:guest@localhost:5672//"


settings = Settings()
