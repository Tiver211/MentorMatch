import os
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from .base_model import Offer
from datetime import datetime, timedelta
import jwt
from fastapi.responses import JSONResponse
from ...database import get_db, User_table, Mentor_table, Offer_table
from uuid import uuid4

post_offer_router = APIRouter()

@post_offer_router.post("mentors/offer")
def post_offer(offer: Offer, db: Session = Depends(get_db), authorization: str = Header(...)):
    token = authorization.split(" ")[1]

    user_data = jwt.decode(token, os.getenv("RANDOM_SECRET"), algorithms=['HS256'])

    mentor = db.query(Mentor_table).filter(Mentor_table.login == offer.mentor_login).first()

