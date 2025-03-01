import os

import jwt
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from .base_model import Offer
from ...database import get_db, User_table, Mentor_table

post_offer_router = APIRouter()

@post_offer_router.post("mentors/offer")
def post_offer(offer: Offer, db: Session = Depends(get_db), authorization: str = Header(...)):
    token = authorization.split(" ")[1]

    user_data = jwt.decode(token, os.getenv("RANDOM_SECRET"), algorithms=['HS256'])

    user = db.query(User_table).filter(User_table.user_id == user_data["user_id"])
    mentor = db.query(Mentor_table).filter(Mentor_table.login == offer.mentor_login).first()

