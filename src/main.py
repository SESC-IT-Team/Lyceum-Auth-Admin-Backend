from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.auth import router as auth_router
from src.routers.proxy import router as proxy_router
from src.routers.health import router as health_router
from src.config import settings
app = FastAPI(root_path=settings.root_path)
app.add_middleware(
	CORSMiddleware,
	allow_origins=settings.allowed_origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(proxy_router, prefix="/proxy/user-service")
app.include_router(health_router, prefix="/health")