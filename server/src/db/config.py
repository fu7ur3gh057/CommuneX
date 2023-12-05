from src.settings import settings

MODELS_MODULES: list[str] = [
    "src.db.models.user_model",
    "src.db.models.project_model",
    "src.db.models.client_model",
    "src.db.models.room_model",
    "src.db.models.message_model",
]  # noqa: WPS407

TORTOISE_CONFIG = {  # noqa: WPS407
    "connections": {
        "default": str(settings.db_url),
    },
    "apps": {
        "models": {
            "models": MODELS_MODULES + ["aerich.models"],
            "default_connection": "default",
        },
    },
}
