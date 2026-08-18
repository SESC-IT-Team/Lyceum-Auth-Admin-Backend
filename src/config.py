from pydantic_settings import BaseSettings, SettingsConfigDict
from sesc_auth_sdk.settings import TokenValidationSettings, AuthRouterSettings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    token_validation_settings: TokenValidationSettings = TokenValidationSettings(_env_file=".env")
    auth_router_settings: AuthRouterSettings = AuthRouterSettings(_env_file=".env")
    user_service_url: str

settings = Settings()