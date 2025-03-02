import os

import uvicorn
from fastapi import FastAPI

from .database import init_db
from .user.user_router import user_router
from .offer.offer_router import offer_router

app = FastAPI()

app.include_router(user_router)
app.include_router(offer_router)

@app.on_event("startup")
def start():
    init_db()

if __name__ == "__main__":
    server_address = os.getenv("SERVER_ADDRESS", "0.0.0.0:443")
    host, port = server_address.split(":")
    uvicorn.run(app, host=host, port=int(port))