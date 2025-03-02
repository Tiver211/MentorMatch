import json
import os
from datetime import datetime, timedelta

from fastapi import Query

import jwt
import redis
from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session

from api.user.sign_up.base_model import User
from api.database import get_db, User_table, get_cache

user_verification = APIRouter(prefix="/user")


@user_verification.get("/verify")
def verify(db: Session = Depends(get_db), redis_client: redis.Redis = Depends(get_cache), token: str = Query(...)):
    user_id = redis_client.get(token)
    user = db.query(User_table).get(user_id)
    if not user:
        return  JSONResponse(status_code=404, content={"status": "verification request doesn't exists"})

    user.is_active = True

    db.commit()

    data = \
        {
            "user_id": str(user.user_id),
            "login": user.login
        }

    token_payload = {
        "sub": data,
        "exp": datetime.utcnow() + timedelta(days=365)
    }

    return RedirectResponse("https://prod-team-35-lg7sic6v.final.prodcontest.ru/login")
