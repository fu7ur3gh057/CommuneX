from typing import Awaitable, Callable

from fastapi import FastAPI

# from sqladmin import Admin
# from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine
#
# from src.services.rabbit.lifetime import init_rabbit, shutdown_rabbit
# from src.services.redis.lifetime import init_redis, shutdown_redis
# from src.settings import settings
# from src.scheduler.tkq import broker
# from src.web.socketio.lifetime import init_socketio, shutdown_socketio


# def _setup_db(app: FastAPI) -> AsyncEngine:  # pragma: no cover
#     engine = create_async_engine(str(settings.db_url), echo=settings.db_echo)
#     session_factory = async_sessionmaker(
#         engine,
#         expire_on_commit=False,
#     )
#     app.state.db_engine = engine
#     app.state.db_session_factory = session_factory
#     return app.state.db_engine


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    @app.on_event("startup")
    async def _startup() -> None:  # noqa: WPS430
        app.middleware_stack = None
        # if not broker.is_worker_process:
        #     await broker.startup()
        # # engine = _setup_db(app)
        # init_redis(app)
        # init_rabbit(app)
        # await init_socketio(app)
        app.middleware_stack = app.build_middleware_stack()
        pass  # noqa: WPS420

    return _startup


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    @app.on_event("shutdown")
    async def _shutdown() -> None:  # noqa: WPS430
        # if not broker.is_worker_process:
        #     await broker.shutdown()
        # # await app.state.db_engine.dispose()
        #
        # await shutdown_redis(app)
        # await shutdown_rabbit(app)
        # await shutdown_socketio(app)
        pass  # noqa: WPS420

    return _shutdown
