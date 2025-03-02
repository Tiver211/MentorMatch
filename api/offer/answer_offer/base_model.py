from pydantic import BaseModel
from pydantic import UUID


class Answer(BaseModel):
    status: bool
    offer_id: UUID