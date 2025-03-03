from pydantic import BaseModel
from uuid import UUID

class Response_user(BaseModel):
    user_id: UUID
    first_name: str
    last_name: str
    age: int
    about: str
    contact: str