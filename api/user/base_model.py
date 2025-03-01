from pydantic import BaseModel, Field

class User(BaseModel):
    first_name: str
    last_name: str
    age: int = Field(ge=0)
    school: str