from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from bson import ObjectId
from app.src.type.type import StageEnum  # Assuming StageEnum is defined elsewhere

class IdeaModel(BaseModel):
    # Optional _id (auto-generated by MongoDB)
    id: Optional[str] = Field(alias="_id")
    
    idea: str
    email: EmailStr
    tags: List[str]
    vector: Optional[List[float]] = None  # This will be generated if not provided
    details: Optional[object] = None
    stage: StageEnum = StageEnum.idea  # Assuming StageEnum is already defined elsewhere

    class Config:
        # Use alias for _id and ensure the type ObjectId is correctly serialized to string
        validate_by_name = True  # Ensures validation is based on the attribute names
        arbitrary_types_allowed = True  # Allowing BSON ObjectId to be used
        json_encoders = {
            ObjectId: str  # Convert BSON ObjectId to string in JSON responses
        }