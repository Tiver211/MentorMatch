import os

import jwt
from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from .base_model import User
from api.database import get_db, User_table

user_update_data_patch = APIRouter()

@user_update_data_patch.patch("/user/profile")
def post_user(user: User, db: Session = Depends(get_db), authorization: str = Header(...)):
    token = authorization.split(" ")[1]

    data = jwt.decode(token, os.getenv("RANDOM_SECRET"), algorithms=['HS256'])

    user_db = db.query(User_table).filter(User_table.user_id == data["sub"]).first()

    user_db.first_name = user.first_name if user.first_name else user_db.first_name
    user_db.last_name = user.last_name if user.last_name else user_db.last_name
    user_db.about = user.about if user.about else user_db.about
    db.commit()

    result = \
        {
            "user_id": str(user_db.user_id),
            "first_name": user_db.first_name,
            "last_name": user_db.last_name,
            "age": user_db.age,
            "about": user_db.about,
            "contact": user_db.contact
        }

    return JSONResponse(status_code=200, content=result)

