from fastapi import Request
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import Session, create_engine, SQLModel

from app.internal.secrets import secrets


engine = create_engine(url=secrets.DATABASE_URL, echo=True)



def db_client_get():
   with Session(engine) as session:
      yield session
