import os
from datetime import datetime, timedelta

import bcrypt
import jwt
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from api.database import get_db, User_table
from api.user.sign_in.base_model import User
from api.mail.mail import send_email

user_auth_sign_in_router = APIRouter()

@user_auth_sign_in_router.post("/user/auth/sign-in")
def post_user(user: User, db: Session = Depends(get_db)):
    user_db = db.query(User_table).filter(User_table.login == user.login).first()

    if not user_db:
        return JSONResponse(status_code=404, content={"status": "User was not found"})

    if not(bcrypt.checkpw(user.password.encode("utf-8"), bytes(user_db.password, "utf-8"))):
        return JSONResponse(status_code=403, content={"status": "Invalid password"})

    data = \
        {
            "user_id": str(user_db.user_id),
            "login": user_db.login
        }

    token_payload = {
        "sub": data,
        "exp": datetime.utcnow() + timedelta(days=365)
    }
    token = jwt.encode(token_payload, os.getenv("RANDOM_SECRET"), algorithm='HS256')

    return JSONResponse(status_code=200, content={"token": token})

