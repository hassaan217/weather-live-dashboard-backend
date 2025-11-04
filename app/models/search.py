# app/models/search.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SearchBase(BaseModel):
    city: str = Field(..., min_length=1, max_length=100)

class SearchCreate(SearchBase):
    pass

class Search(SearchBase):
    id: str = Field(alias="_id")
    timestamp: datetime
    
    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }