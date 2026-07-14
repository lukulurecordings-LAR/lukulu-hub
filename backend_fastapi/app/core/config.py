from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'Lukulu Hub Analytics API'
    app_version: str = '0.1.0'
    environment: str = 'development'
    cors_origins: str = 'http://localhost:3000,https://d79f9e4f13f65eacaa.v2.appdeploy.ai,https://lukulu-hub.vercel.app'
    supabase_url: str = ''
    supabase_publishable_key: str = ''
    supabase_service_role_key: str = ''
    openai_api_key: str = ''
    default_organization_slug: str = 'lukulu-recordings'

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(',') if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
