import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_PAGE_SIZE: int = 20
    USE_LOCAL_STORAGE: bool = False
    MEDIA_PATH: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'public')
    DB_HOST: str = ""


settings = Settings()
