from .sign_in.user_auth_sign_in_post import user_auth_sign_in_router
from .sign_up.user_auth_post import user_auth_post_router
from .update.user_data_update import user_update_data_patch
from fastapi import APIRouter

user_router = APIRouter()
user_router.include_router(user_update_data_patch)
user_router.include_router(user_auth_post_router)
user_router.include_router(user_auth_sign_in_router)