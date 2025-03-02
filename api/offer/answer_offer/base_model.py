from pydantic import BaseModel
from uuid import UUID


class Answer(BaseModel):
    status: bool
    offer_id: UUID