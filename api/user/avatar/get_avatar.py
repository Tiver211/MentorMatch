import os
import jwt
from fastapi.openapi.models import Response
from fastapi.params import Depends, File
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import APIRouter, Query, Header, UploadFile
from typing import Optional
from starlette.responses import JSONResponse, Response, FileResponse
from uuid import UUID
import tempfile
from ...database import get_db, User_table

get_avatar_router = APIRouter()

@get_avatar_router.get("user/avatar/{user_id}")
def get_image(user_id: UUID, db: Session = Depends(get_db)):
    user: User_table | None = db.query(User_table).filter(User_table.user_id == user_id).first()

    if not user:
        return JSONResponse(status_code=404, content={"status": "User not found"})

    avatar = user.avatar

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(avatar)
        temp_file_path = temp_file.name

    return FileResponse(temp_file_path, media_type="image/png", filename="image.png")

@get_avatar_router.put("user/avatar")
def send_image(file: bytes = File(), db: Session = Depends(get_db), authorization: str = Header(...)):
    token = authorization.split(" ")[1]

    data = jwt.decode(token, os.getenv("RANDOM_SECRET"), algorithms=['HS256'])

    user_db = db.query(User_table).filter(User_table.user_id == data["sub"]).first()

    if not user_db:
        return JSONResponse(status_code=404, content={"status": "User not found"})

    user_db.avatar = file

    db.commit()

    return JSONResponse(status_code=200, content={"status": "OK"})

