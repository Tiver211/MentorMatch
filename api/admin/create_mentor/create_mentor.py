import os

import jwt

from ...database import get_db, Mentor_table, User_table, Admin_table
from .base_model import Mentor
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import APIRouter, Query, Header
from typing import Optional
from starlette.responses import JSONResponse
import datetime
from uuid import UUID, uuid4
from api.mail.mail import send_email

create_menter_router = APIRouter()

@create_menter_router.post("/admin/user/{user_id}/mentor")
def crete_mentor(mentor: Mentor, user_id: UUID, db: Session = Depends(get_db), authorization: str = Header(...)):
    token = authorization.split(" ")[1]

    data = jwt.decode(token, os.getenv("RANDOM_SECRET"), algorithms=['HS256'])

    admin = db.query(Admin_table).filter(Admin_table.admin_id == data["admin_id"]).first()

    if not admin:
        return JSONResponse(status_code=403, content={"status": "Admin was not found or you are not admin"})

    user = db.query(User_table).filter(User_table.user_id == user_id).first()

    if not user:
        return JSONResponse(status_code=404, content={"status": "User not found"})

    new_mentor = Mentor_table(mentor_id=uuid4(), user_id=user_id, direction=mentor.direction)

    db.add(new_mentor)
    db.commit()

    return JSONResponse(status_code=201, content={"mentor_id": str(new_mentor.mentor_id)})
