import json
import time

from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/health")
def health_check() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    # await hello_task.kiq(1)
