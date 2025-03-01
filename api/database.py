from sqlalchemy.dialects.postgresql import UUID as UUIDP
from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from uuid import UUID
import os

Base = declarative_base()

DATABASE_URL = os.getenv("POSTGRES_CONN")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User_table(Base):
    __tablename__ = "users"

    user_id: UUID = Column(UUIDP(as_uuid=True), primary_key=True)
    login: str = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    first_name: str = Column(String, nullable=False)
    last_name: str = Column(String, nullable=False)
    age: int = Column(Integer, nullable=False)
    about: str = Column(Text, nullable=True)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)