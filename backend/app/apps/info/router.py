from fastapi import APIRouter
import socket

info_router = APIRouter()
from settings import settings
from apps.info.schemas import BaseBackendInfoSchema, DatabaseInfoSchema

@info_router.get("/hostname")
async def get_backend() -> BaseBackendInfoSchema:
    return BaseBackendInfoSchema(backend=socket.gethostname())

@info_router.get("/database")
async def get_database() -> DatabaseInfoSchema:
    return DatabaseInfoSchema(database_url=settings.DATABASE_ASYNC_URL)
