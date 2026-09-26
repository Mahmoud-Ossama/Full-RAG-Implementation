from fastapi import FastAPI 
from routes import base, data
from pymongo import AsyncMongoClient
from helpers.config import get_settings

app = FastAPI()

@app.on_event("startup")
async def startup_client():
    settings = get_settings()
    # Initialize the MongoDB client
    app.mongo_conn = AsyncMongoClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]    
    
@app.on_event("shutdown")
async def shutdown_client():
    if app.mongo_conn:
        await app.mongo_conn.close()
    if app.db_client:
        await app.db_client.close()

app.include_router(base.router)
app.include_router(data.data_router)





# @app.get("/")
# async def read_root():
#     return {"message": "Hello, World!"}
