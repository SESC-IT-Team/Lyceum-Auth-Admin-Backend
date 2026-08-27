import os
import ssl

from sesc_auth_sdk.dependencies import (
    LyceumAuth,
    create_jwks_manager_dependency,
)

from sesc_auth_sdk.services.jwks_manager import JWKSManager
from sesc_auth_sdk.settings import TokenValidationSettings
from src.config import settings

import aiohttp

jwks_manager = JWKSManager(settings.token_validation_settings)

class Auth(LyceumAuth):
    get_jwks_manager = create_jwks_manager_dependency(
        jwks_manager
    )

async def get_session():
    ssl_context = ssl.create_default_context(
        cafile=os.getenv("SSL_CERT_FILE")
    )
    connector = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=connector) as session:
        yield session