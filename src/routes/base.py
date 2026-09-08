from fastapi import FastAPI, APIRouter, Depends
# import os
from helpers.config import get_settings, Settings

# settings = get_settings()

router = APIRouter(
    prefix="/api/v1",
    tags=["Base"]
)

@router.get("/")
async def read_root(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
        "message": "From World Wide Developer!"
        }
