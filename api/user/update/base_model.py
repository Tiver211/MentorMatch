from typing import Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    about: Optional[str]