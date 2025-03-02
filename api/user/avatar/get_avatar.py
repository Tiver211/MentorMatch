import os
import jwt
from fastapi.openapi.models import Response
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import APIRouter, Query, Header
from typing import Optional
from starlette.responses import JSONResponse, Response, FileResponse
from uuid import UUID
import tempfile
from ...database import get_db, User_table

get_avatar_router = APIRouter()

@get_avatar_router.get("user/avatar/{user_id}")
def get_image(user_id: UUID, db: Session = Depends(get_db), authorization: str = Header(...)):
    user: User_table | None = db.query(User_table).filter(User_table.user_id == user_id).first()

    if not user:
        return JSONResponse(status_code=404, content={"status": "User not found"})

    avatar = user.avatar

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(avatar)
        temp_file_path = temp_file.name

    return FileResponse(temp_file_path, media_type="image/png", filename="image.png")

