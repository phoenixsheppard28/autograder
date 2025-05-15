from sqlmodel import Session, create_engine,SQLModel
from app.internal.secrets import secrets
from app.dependencies.db_dep import engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine,checkfirst=False)

def dispose_db():
    engine.dispose()
