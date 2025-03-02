from pydantic import BaseModel, List, Field


class Request(BaseModel):
    about: str = Field(min_length=100, max_length=2000)
    directions: List[str]