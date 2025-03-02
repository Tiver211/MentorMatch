import os
from datetime import datetime, timedelta

import bcrypt
import jwt
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from .base_model import Admin
from ...database import get_db, Admin_table

admin_auth_sign_in_router = APIRouter()

@admin_auth_sign_in_router.post("/admin/secret-url")
def post_admin(admin: Admin, db: Session = Depends(get_db)):
    admin_db = db.query(Admin_table).filter(Admin_table.login == admin.login).first()

    if not admin_db:
        return JSONResponse(status_code=404, content={"status": "Admin was not found"})

    if not(bcrypt.checkpw(admin.password.encode(), bytes(admin_db.password, "utf-8"))):
        return JSONResponse(status_code=403, content={"status": "Invalid password"})

    data = \
        {
            "admin_id": str(admin_db.admin_id),
            "login": admin_db.login
        }

    token_payload = {
        "sub": data,
        "exp": datetime.utcnow() + timedelta(days=365)
    }
    token = jwt.encode(token_payload, os.getenv("RANDOM_SECRET"), algorithm='HS256')

    return JSONResponse(status_code=200, content={"token": token})

