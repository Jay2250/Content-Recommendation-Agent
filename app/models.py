from pydantic import BaseModel
from typing import List

class UserRequest(BaseModel):
    user_id: str
    interests: List[str]

class ContentResponse(BaseModel):
    user_id: str
    recommendations: List[str]
