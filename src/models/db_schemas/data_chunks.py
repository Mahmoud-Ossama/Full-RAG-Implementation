from pydantic import BaseModel, Field, validator
from typing import Optional
from bson import ObjectId

class DataChunks(BaseModel):
    id: Optional[ObjectId]
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    

    # Allow arbitrary types for pydantic models to not get error for id
    class Config:
        arbitrary_types_allowed = True