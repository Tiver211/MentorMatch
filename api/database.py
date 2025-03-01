from sqlalchemy.dialects.postgresql import UUID as UUIDP
from sqlalchemy import Column, Integer, String, Text, BINARY, ARRAY, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, foreign
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
    password: str = Column(BINARY, nullable=False)
    first_name: str = Column(String, nullable=False)
    last_name: str = Column(String, nullable=False)
    age: int = Column(Integer, nullable=False)
    about: str = Column(Text, nullable=True)

class Mentor_table(Base):
    __tablename__ = "mentors"

    mentor_id: UUID = Column(UUIDP(as_uuid=True), primary_key=True)
    login: str = Column(String, nullable=False, unique=True)
    password: str = Column(BINARY, nullable=False)
    first_name: str = Column(String, nullable=False)
    last_name: str = Column(String, nullable=False)
    age: int = Column(Integer, nullable=False)
    about: str = Column(Text, nullable=False)
    direction: str = Column(ARRAY(String), nullable=False)

class Mentors_requests_table(Base):
    __tablename__ = "mentorRequests"

    request_id: UUID = Column(UUIDP(as_uuid=True), primary_key=True)
    about: str = Column(Text, nullable=False)
    direction: str = Column(ARRAY(String), nullable=False)

class Offer_table(Base):
    __tablename__ = "offers"

    offer_id: UUID = Column(UUIDP(as_uuid=True), primary_key=True)
    mentor_id: UUID = Column(UUIDP(as_uuid=True), ForeignKey('mentors.mentor_id', ondelete='CASCADE'), nullable=False)
    user_id: UUID = Column(UUIDP(as_uuid=True), ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    message: str = Column(Text, nullable=True)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)