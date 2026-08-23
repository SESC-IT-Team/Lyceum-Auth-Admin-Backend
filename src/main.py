from fastapi import FastAPI
from src.routers.auth import router as auth_router
from src.routers.proxy import router as proxy_router
from src.routers.health import router as health_router
from src.config import settings
app = FastAPI(root_path=settings.root_path)

app.include_router(auth_router, prefix="/auth")
app.include_router(proxy_router, prefix="/proxy/user-service")
app.include_router(health_router, prefix="/health")