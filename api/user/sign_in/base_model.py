from pydantic import BaseModel, Field

class User(BaseModel):
    login: str
    password: str