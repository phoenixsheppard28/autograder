from fastapi import FastAPI , Depends
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from typing import Annotated
from app.dependencies.db_dep import db_client_get
from app.internal.database import create_db_and_tables, dispose_db
import uvicorn
from sqlmodel import Session, select, insert
from app.models import models





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

@app.get("/api/users")
async def list_users(db: Annotated[Session, Depends(db_client_get)]):
   
    response = db.exec(select(models.Autograder_Logs)).first()
    return response

# @app.post("/api/user")
# async def create_user(user:models.)







@app.post("/log")
async def create_log(sess:Annotated[Session,Depends(db_client_get)]): # change the way this is, maybe it should be done not as an endpoint but as a function called by other processes
    try:
        # sess.add(log)
        sess.commit()
        return {"status": "success"}
    except Exception as e:
        print(e) # server side
        return JSONResponse(status_code=400, content={"error": "idk"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
