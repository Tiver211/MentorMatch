import datetime

from fastapi.params import Depends, Header
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import APIRouter, Query
from typing import Optional
import os
import jwt
from starlette.responses import JSONResponse
from uuid import UUID, uuid4

from .base_model import Request
from ...database import get_db, User_table, Mentors_requests_table

send_request_router = APIRouter()

@send_request_router.post("/mentors/request")
def send_request(request: Request, db: Session = Depends(get_db), authorization: str = Header(...)):
    token = authorization.split(" ")[1]

    data = jwt.decode(token, os.getenv("RANDOM_SECRET"), algorithms=['HS256'])

    new_request = Mentors_requests_table(request_id=uuid4(), user_id=data["user_id"], about=request.about, direction=request.directions, date=datetime.datetime.now(), status=False)

    db.add(new_request)
    db.commit()

    return JSONResponse(status_code=201, content={"request_id": f"{new_request.request_id}"})
