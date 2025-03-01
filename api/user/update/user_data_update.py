import os
import bcrypt
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from fastapi.responses import JSONResponse
from ...database import get_db, User_table
from uuid import uuid4

from api.user.sign_up.base_model import User

user_update_data_patch = APIRouter()

@user_update_data_patch.patch("/user/profile")
def post_user(user: User, db: Session = Depends(get_db), authorization: str = Header(...)):
    token = authorization.split(" ")[1]

    data = jwt.decode(token, algorithms="HS256")

    user_db = db.query(User_table).filter(User_table.login == data.login).first()

    user_db.first_name = user.first_name if user.first_name else user_db.first_name
    user_db.last_name = user.last_name if user.last_name else user_db.last_name
    user_db.age = user.age if user.age else user_db.age

    return JSONResponse(status_code=200, content=data)

