from fastapi import APIRouter
from .answer_offer.answer_offer import answer_offer_router
from .post_offer.post_offer import post_offer_router

offer_router = APIRouter()

offer_router.include_router(answer_offer_router)
offer_router.include_router(post_offer_router)