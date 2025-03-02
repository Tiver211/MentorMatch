from pydantic import BaseModel, Field
from typing import List

class Request(BaseModel):
    about: str = Field(min_length=100, max_length=2000)
    directions: List[str]