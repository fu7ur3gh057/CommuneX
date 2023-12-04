import uvicorn
from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from src.settings import settings

app = FastAPI(
    title="CommuneX API",
    docs_url=f"{settings.api_prefix}/docs",
    redoc_url=f"{settings.api_prefix}/redoc",
    openapi_url=f"{settings.api_prefix}/openapi.json",
    default_response_class=UJSONResponse,
)


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "src.web.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()
