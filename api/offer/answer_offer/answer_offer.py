from uuid import UUID, uuid4

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from .models.base_model import Answer
from .models.response_model import Response_offer
from ...database import get_db, User_table, Mentor_table, Offer_table, Students_table

answer_offer_router = APIRouter()

@answer_offer_router.post("/mentors/{mentor_id}/offers/{user_id}", status_code=200, response_model=Response_offer)
def answer_offer(answer: Answer, mentor_id: UUID, user_id: UUID, db: Session = Depends(get_db)):
    user = db.query(User_table).filter(User_table.user_id == user_id).first()

    if not user:
        return JSONResponse(status_code=404, content={"status": "User not found"})

    mentor = db.query(User_table).join(Mentor_table).filter(User_table.user_id == Mentor_table.user_id, Mentor_table.mentor_id == mentor_id).first()

    if not mentor:
        return JSONResponse(status_code=404, content={"status": "Mentor not found"})

    if answer.status:
        # send_email("Your offer was accepted", f"Contact of mentor {mentor.contact}", user.contact)

        new_student = Students_table(id=uuid4(), mentor_id=mentor_id, user_id=user_id)

        offer = db.query(Offer_table).filter(Offer_table.offer_id == answer.offer_id).first()

        offer.status = True

        db.add(new_student)
        db.commit()

        result = \
            {
                "offer_id": f"{offer.offer_id}",
                "mentor_id": f"{offer.mentor_id}",
                "user_id": f"{offer.user_id}",
                "message": f"{offer.message}",
                "date": offer.date
            }

        return result

    else:
        # send_email("Your offer was not accepted", f"Sorry but mentor does not accepted your offer", user.contact)
        offer = db.query(Offer_table).filter(Offer_table.offer_id == answer.offer_id).first()

        offer.status = False

        db.commit()

        return JSONResponse(status_code=200, content={"status": "Mentor does not accepted offer"})