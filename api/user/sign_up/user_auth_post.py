import os
import bcrypt
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from fastapi.responses import JSONResponse
from ...database import get_db, User_table
from uuid import uuid4

from api.user.sign_up.base_model import User

user_auth_post_router = APIRouter()

@user_auth_post_router.post("/user/auth/sign-up")
def post_user(user: User, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt(rounds=4))

    new_user = User_table(
        user_id=uuid4(),
        login=user.login,
        password=str(hashed_password),
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
        about=user.about
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    data = \
        {
            "user_id": str(new_user.user_id),
            "login": new_user.login
        }

    token_payload = {
        "sub": data,
        "exp": datetime.utcnow() + timedelta(days=365)
    }
    token = jwt.encode(token_payload, os.getenv("RANDOM_SECRET"), algorithm='HS256')

    return JSONResponse(status_code=201, content={"token": token})

