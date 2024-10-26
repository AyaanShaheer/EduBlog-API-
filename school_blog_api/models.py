from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Post(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    content: str = Field(..., min_length=10)
    author: str = Field(..., min_length=3, max_length=50)
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
