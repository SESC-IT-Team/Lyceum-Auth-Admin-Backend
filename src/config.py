import json
import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import dotenv_values
from sesc_auth_sdk.settings import TokenValidationSettings, AuthRouterSettings


def normalize_allowed_issuers() -> None:
    raw_value = os.getenv("ALLOWED_ISSUERS")
    if not raw_value:
        return

    try:
        parsed_value = json.loads(raw_value)
    except json.JSONDecodeError:
        parsed_value = [item.strip() for item in raw_value.split(",") if item.strip()]

    if isinstance(parsed_value, str):
        parsed_value = [parsed_value]

    os.environ["ALLOWED_ISSUERS"] = json.dumps(parsed_value)


def normalize_allowed_origins() -> None:
    raw_value = os.getenv("ALLOWED_ORIGINS") or dotenv_values(".env").get("ALLOWED_ORIGINS")
    if not raw_value:
        return

    try:
        parsed_value = json.loads(raw_value)
    except json.JSONDecodeError:
        parsed_value = [item.strip() for item in raw_value.split(",") if item.strip()]

    if isinstance(parsed_value, str):
        parsed_value = [parsed_value]

    os.environ["ALLOWED_ORIGINS"] = json.dumps(parsed_value)


normalize_allowed_issuers()
normalize_allowed_origins()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    token_validation_settings: TokenValidationSettings = TokenValidationSettings(_env_file=".env")
    auth_router_settings: AuthRouterSettings = AuthRouterSettings(_env_file=".env")
    user_service_url: str
    root_path: str = "/"
    allowed_origins: list[str] = []

settings = Settings()