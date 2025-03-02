from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import APIRouter, Query
from uuid import UUID

from starlette.responses import JSONResponse

from ...database import get_db, User_table, Mentor_table

get_mentor_router = APIRouter()

@get_mentor_router.get("mentors/{mentor_id}")
def get_mentor(mentor_id: UUID, db: Session = Depends(get_db)):
    mentor = db.query(Mentor_table).filter(Mentor_table.mentor_id == mentor_id).first()

    if not mentor:
        return JSONResponse(status_code=404, content={"status": "Mentor not found"})

    user = db.query(User_table).filter(User_table.user_id == mentor.user_id).first()

    result = \
        {
            "mentor_id": str(mentor.mentor_id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "direction": mentor.direction,
            "about": user.about,
            "contact": user.contact
        }


    return JSONResponse(status_code=200, content=result)