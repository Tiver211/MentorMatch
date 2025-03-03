import os
import jwt
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import APIRouter, Query, Header
from typing import Optional
from starlette.responses import JSONResponse
from uuid import UUID

from ...database import get_db, User_table

get_profile_router = APIRouter()

@get_profile_router.get("/user/profile")
def get_users(db: Session = Depends(get_db), authorization: str = Header(...)):
    token = authorization.split(" ")[1]

    data = jwt.decode(token, os.getenv("RANDOM_SECRET"), algorithms=['HS256'])

    user = db.query(User_table).filter(User_table.user_id == data["sub"]).first()

    if not user:
        return JSONResponse(status_code=404, content={"status": "User not found"})

    result = \
        {
            "user_id": str(user.user_id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "about": user.about,
            "contact": user.contact,
            "avatar": f"https://prod-team-35-lg7sic6v.final.prodcontest.ru/api/user/avatar/{str(user.user_id)}" if user.avatar is not None else None
        }

    return JSONResponse(status_code=200, content=result)