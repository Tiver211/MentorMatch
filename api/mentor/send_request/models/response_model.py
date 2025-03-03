from pydantic import BaseModel
from uuid import UUID
import datetime

class Response_request(BaseModel):
    request_id: UUID
    user_id: UUID
    about: str
    direction: str
    date: datetime.datetime
    status: bool