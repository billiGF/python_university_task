from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_title: str
    database: str

    class Config:
        env_file = '.env'


settings = Settings()