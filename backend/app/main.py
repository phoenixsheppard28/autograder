from fastapi import FastAPI ,Depends
from contextlib import asynccontextmanager
from typing import Annotated
from app.dependencies.db_dep import db_client_get
from app.internal.database import create_db_and_tables, dispose_db
import uvicorn
from sqlmodel import Session, select
from app.models.models import Test



@asynccontextmanager
async def db_lifespan(app: FastAPI): # want to make this not dependent on a specific database
    try:
        create_db_and_tables()
        print("Database client connected!")
        yield
    finally:
        dispose_db()
        print("Shutting down Database client...")

app = FastAPI(lifespan=db_lifespan)

@app.get("/users")
async def list_users(db: Annotated[Session, Depends(db_client_get)]):
   
    response = db.exec(select(Test)).first()
    return response



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
