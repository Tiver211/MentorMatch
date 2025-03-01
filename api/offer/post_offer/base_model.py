from typing import Optional
from pydantic import BaseModel

class Offer(BaseModel):
    mentor_login: str
    message: Optional[str] = None