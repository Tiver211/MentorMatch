import datetime
import os
from uuid import uuid4

import jwt
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from .base_model import Offer
from ...database import get_db, User_table, Offer_table, Mentor_table

from api.mail.mail import send_email

post_offer_router = APIRouter()

@post_offer_router.post("/mentors/offer")
def post_offer(offer: Offer, db: Session = Depends(get_db), authorization: str = Header(...)):
    token = authorization.split(" ")[1]

    user_data = jwt.decode(token, os.getenv("RANDOM_SECRET"), algorithms=['HS256'])

    user = db.query(User_table).filter(User_table.user_id == user_data["sub"]).first()
    mentor = db.query(Mentor_table).join(User_table).filter(User_table.login == offer.mentor_login, User_table.user_id == Mentor_table.user_id).first()

    new_offer = Offer_table(offer_id=uuid4(), mentor_id=mentor.mentor_id, user_id=user.user_id, message=offer.message, date=datetime.datetime.now())

    db.add(new_offer)
    db.commit()

    mentor_contact = db.query(User_table).filter(User_table.user_id == mentor.user_id).first()

    # send_email("New offer", f"You have received an offer from {user.contact}", mentor_contact.contact)

    return JSONResponse(status_code=200, content={"status": "ok"})
