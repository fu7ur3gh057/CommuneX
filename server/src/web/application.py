from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from main import app
from src.db.config import TORTOISE_CONFIG
from src.web.api.router import api_router

# from src.web.api.router import api_router
from src.web.lifetime import (
    register_shutdown_event,
    register_startup_event,
)
from src.settings import settings


def get_app() -> FastAPI:
    # Add Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix=settings.api_prefix)
    # Configures tortoise orm.
    register_tortoise(
        app,
        config=TORTOISE_CONFIG,
        add_exception_handlers=True,
    )
    return app
