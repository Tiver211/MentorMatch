import os

import bcrypt
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from sqlalchemy.orm import Session
from uuid import uuid4
from .database import init_db, Admin_table, SessionLocal
from .user.user_router import user_router
from .offer.offer_router import offer_router
from .admin.admin_router import admin_router
from .mentor.mentor_router import mentor_router

app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://prod-team-35-lg7sic6v.final.prodcontest.ru", "https://localhost"],  # Разрешить все домены (или укажите конкретные, например ["https://example.com"])
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

app.include_router(user_router)
app.include_router(offer_router)
app.include_router(admin_router)
app.include_router(mentor_router)

@app.on_event("startup")
def start():
    init_db()

    db: Session = SessionLocal()

    admin_exists = db.query(Admin_table).filter(Admin_table.login == "admin").first()
    if not admin_exists:
        hashed_password = bcrypt.hashpw("test".encode(), bcrypt.gensalt(rounds=4))

        admin = Admin_table(
            admin_id=uuid4(),
            login="admin",
            password=hashed_password.decode()
        )
        db.add(admin)
        db.commit()
    db.close()

#@app.get("/ping")
#def ping():
#    return JSONResponse(status_code=200, content="PROOOOOOOOOOD")

if __name__ == "__main__":
    server_address = os.getenv("SERVER_ADDRESS", "0.0.0.0:443")
    host, port = server_address.split(":")
    uvicorn.run(app, host=host, port=int(port))