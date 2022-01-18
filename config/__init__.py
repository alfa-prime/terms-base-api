from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """
    Project settings, values gets from .env
    https://fastapi.tiangolo.com/advanced/settings/
    https://pydantic-docs.helpmanual.io/usage/settings/
    """
    app_title: str = Field(..., env="APP_TITLE")
    api_description: str = Field(..., env="API_DESCRIPTION")
    api_ver_prefix: str = Field(..., env="API_VER_PREFIX")
    api_doc_endpoint: str = Field(..., env="API_DOC_ENDPOINT")

    database_url: str = Field(..., env="DATABASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
