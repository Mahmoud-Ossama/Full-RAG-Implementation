from pydantic import BaseModel, Field, validator
from typing import Optional
from bson import ObjectId

class Project(BaseModel):
    id: Optional[ObjectId]
    project_id: str = Field(..., min_length=1)
    
    @validator("project_id")
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError("Project ID must be alphanumeric")
        return value
    
    # Allow arbitrary types for pydantic models to not get error for id
    class Config:
        arbitrary_types_allowed = True