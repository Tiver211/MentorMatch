import datetime
from pydantic import BaseModel
from uuid import UUID

class Response_offer(BaseModel):
    mentor_id: UUID
    user_id: UUID
    message: str
    status: bool
    date: datetime.datetime