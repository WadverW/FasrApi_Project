from fastapi import FastAPI
import socket
from settings import settings

def get_application() -> FastAPI:

    app = FastAPI(
        root_path="/api",
        debug = settings.DEBUG,
        title = settings.APP_NAME,
    )

    @app.get("/info")
    async def get_backend():
        return {"backend": socket.gethostname()}

    return app