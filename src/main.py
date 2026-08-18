from fastapi import FastAPI
from src.routers.auth import router as auth_router
from src.routers.proxy import router as proxy_router
from src.routers.health import router as health_router

app = FastAPI()

app.include_router(auth_router, prefix="/api/auth")
app.include_router(proxy_router, prefix="/api/proxy/user-service")
app.include_router(health_router, prefix="/api/health")