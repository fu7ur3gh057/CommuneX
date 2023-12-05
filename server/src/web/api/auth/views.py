import json
import time

from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/register")
async def register_view():
    pass


@router.post("/login")
async def login_view():
    pass


@router.post("/refresh")
async def refresh_view():
    pass
