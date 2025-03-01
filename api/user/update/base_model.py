from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    first_name: Optional[str]= None
    last_name: Optional[str] = None
    about: Optional[str] = None