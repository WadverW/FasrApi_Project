from fastapi import APIRouter
import socket
info_router = APIRouter()
from settings import settings

@info_router.get("/hostname")
async def get_backend():
    return {"backend": socket.gethostname()}

@info_router.get("/database")
async def get_database():
    return {"database": settings.DATABASE_ASYNC_URL()}