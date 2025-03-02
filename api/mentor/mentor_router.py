from fastapi import APIRouter
from .send_request.send_request import send_request_router

mentor_router = APIRouter()

mentor_router.include_router(send_request_router)