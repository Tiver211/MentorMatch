from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import APIRouter, Query
from typing import Optional
from starlette.responses import JSONResponse
import datetime

from ...database import get_db, Mentors_requests_table

get_requests_router = APIRouter()

@get_requests_router.get("admin/secreturl/mentor-requests")
def get_mentor_requests(
    db: Session = Depends(get_db),
    sort_by: Optional[str] = Query(None),
    order: Optional[str] = Query('asc'),
    date_from: Optional[datetime.datetime] = Query(None),
    date_to: Optional[datetime.datetime] = Query(None),
    group_by_status: Optional[bool] = Query(False)
):
    query = db.query(Mentors_requests_table)

    if date_from:
        query = query.filter(Mentors_requests_table.date >= date_from)
    if date_to:
        query = query.filter(Mentors_requests_table.date <= date_to)

    if group_by_status:
        query = query.group_by(Mentors_requests_table.status)

    if sort_by == "date":
        if order == 'asc':
            query = query.order_by(asc(Mentors_requests_table.date))
        else:
            query = query.order_by(desc(Mentors_requests_table.date))
    elif sort_by == "request_id":
        if order == 'asc':
            query = query.order_by(asc(Mentors_requests_table.request_id))
        else:
            query = query.order_by(desc(Mentors_requests_table.request_id))

    requests = query.all()

    result = [
        {
            "request_id": str(request.request_id),
            "about": request.about,
            "direction": request.direction,
            "date": request.date.isoformat(),
            "status": request.status
        }
        for request in requests
    ]

    return JSONResponse(status_code=200, content=result)
