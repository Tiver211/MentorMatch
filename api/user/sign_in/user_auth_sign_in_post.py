import os
from http.client import HTTPException
import bcrypt
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from fastapi.responses import JSONResponse
from api.database import get_db, User_table
from uuid import uuid4

from api.user.sign_in.base_model import User

user_auth_sign_in_router = APIRouter()

@user_auth_sign_in_router.post("/user/auth/sign-in")
def post_user(user: User, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt(rounds=4))

    user_db = db.query(User_table).filter(User_table.login == user.login).first()

    if not user_db:
        return JSONResponse(status_code=404, content={"status": "User was not found"})

    if not(bcrypt.checkpw(user.password.encode(), user_db.password)):
        return JSONResponse(status_code=403, content={"status": "Invalid password"})

    data = \
        {
            "user_id": str(user_db.user_id),
            "login": user_db.login
        }

    token_payload = {
        "sub": data,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(token_payload, os.getenv("RANDOM_SECRET"), algorithm='HS256')

    return JSONResponse(status_code=200, content={"token": token})

