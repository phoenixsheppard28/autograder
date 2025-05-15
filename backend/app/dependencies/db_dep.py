# from sqlmodel.ext.asyncio.session import AsyncSession add when sqlmode includes async
from sqlmodel import Session, create_engine, SQLModel
from app.internal.secrets import secrets


engine = create_engine(url=secrets.DATABASE_URL, echo=False)



def db_client_get():
   with Session(engine) as session:
      yield session
