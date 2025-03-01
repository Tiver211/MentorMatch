from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str
    age: int = Field(ge=0)
    about: Optional[str] = None