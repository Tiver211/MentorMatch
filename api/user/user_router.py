from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from fastapi.responses import JSONResponse
from ..database import get_db, User_table
from uuid import uuid4

from base_model import User

user_router = APIRouter()

@user_router.post("/user/auth")
def post_user(user: User, db: Session = Depends(get_db)):
    new_user = User_table(
        user_id=uuid4(),
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
        school=user.school
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token_payload = {
        "sub": str(new_user.user_id),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(token_payload, "gsugfsgoGYOUF646", algorithm='HS256')

    return JSONResponse(status_code=201, content={"token": token})

