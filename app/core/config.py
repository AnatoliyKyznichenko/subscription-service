import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Явная загрузка .env файла
load_dotenv()

class Settings(BaseSettings):
    DB_PATH: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    POSTGRES_DB: str

    class Config:
        env_file = '.env'


settings = Settings()

POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
DB_HOST=os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
POSTGRES_DB=os.environ.get("POSTGRES_DB")