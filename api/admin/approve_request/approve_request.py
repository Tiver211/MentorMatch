from ...database import get_db, Mentors_requests_table
from .base_model import Approve
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import APIRouter, Query
from typing import Optional
from starlette.responses import JSONResponse
import datetime
from uuid import UUID

approve_router = APIRouter()

@approve_router.post("/admin/secreturl/mentor-requests/{request_id}")
def approve_request(approve: Approve, request_id: UUID, db: Session = Depends(get_db)):
    request = db.query(Mentors_requests_table).filter(Mentors_requests_table.request_id == request_id).first()

    if not request:
        return JSONResponse(status_code=404, content={})