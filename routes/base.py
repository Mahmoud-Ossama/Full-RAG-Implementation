from fastapi import FastAPI, APIRouter
import os

router = APIRouter(
    prefix="/api/v1",
    tags=["Base"]
)

@router.get("/")
async def read_root():
    return {
        "app_name": os.getenv("APP_NAME"),
        "app_version": os.getenv("APP_VERSION"),
        "message": "From World Wide Developer!"
        }
