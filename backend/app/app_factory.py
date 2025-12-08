from sys import prefix

from fastapi import FastAPI
from settings import settings
from apps.info.router import info_router
from apps.users.router import users_router

def get_application() -> FastAPI:

    app = FastAPI(
        root_path="/api",
        debug = settings.DEBUG,
        title = settings.APP_NAME,
    )
    app.include_router(users_router, prefix='/users', tags=["Users"])

    if settings.DEBUG:
        app.include_router(info_router, prefix="/info", tags=["Info"])

    return app