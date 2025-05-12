from fastapi import Request
from sqlmodel import Session
from sqlmodel import Session, create_engine, SQLModel
from app.models.models import Test
from app.internal.secrets import secrets
from app.models import models

engine = create_engine(url=secrets.DATABASE_URL, echo=True)



def db_client_get():
   with Session(engine) as session:
      yield session
