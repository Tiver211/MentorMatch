from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import APIRouter, Query
from typing import Optional
from starlette.responses import JSONResponse

from ...database import get_db, User_table

get_users_router = APIRouter()

@get_users_router.get("/admin/secreturl/users")
def get_users(
    db: Session = Depends(get_db),
    sort_by: Optional[str] = Query(None),
    age_from: Optional[int] = Query(0),
    age_to: Optional[int] = Query(999),
    order: Optional[str] = Query('asc')
):
    query = db.query(User_table).filter(User_table.age <= age_to, User_table.age >= age_from)

    if sort_by == "name":
        if order == 'asc':
            query = query.order_by(asc(User_table.first_name), asc(User_table.last_name))
        else:
            query = query.order_by(desc(User_table.first_name), desc(User_table.last_name))
    elif sort_by == "age":
        if order == 'asc':
            query = query.order_by(asc(User_table.age))
        else:
            query = query.order_by(desc(User_table.age))

    users = query.all()

    result = [
        {
            "user_id": str(user.user_id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "about": user.about,
            "contact": user.contact,
            "avatar": f"https://prod-team-35-lg7sic6v.final.prodcontest.ru/api/user/avatar/{str(user.user_id)}" if user.avatar is not None else None
        }
        for user in users
    ]

    return JSONResponse(status_code=200, content=result)