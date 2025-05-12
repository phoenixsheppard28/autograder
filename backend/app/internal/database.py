from sqlmodel import Session, create_engine,SQLModel
from app.internal.secrets import secrets
from app.dependencies.db_dep import engine
from app.models.models import Test

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def dispose_db():
    engine.dispose()
