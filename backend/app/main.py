from fastapi import FastAPI ,Depends
from supabase import AsyncClient, create_async_client
from app.internal.secrets import DBsecrets
from contextlib import asynccontextmanager
from typing import Annotated
from app.dependencies.dependencies import db_client_get


@asynccontextmanager
async def db_lifespan(app: FastAPI):
    try:
        global supabase
        app.state.supabase  = await create_async_client(DBsecrets.SUPABASE_URL,DBsecrets.SUPABASE_KEY)
        print("Supabase client connected!")
        yield
    finally:
        print("Shutting down Supabase client...")

app = FastAPI(lifespan=db_lifespan)

@app.get("/users")
async def list_users(db: Annotated[AsyncClient, Depends(db_client_get)]):
   
    response = await db.table("users").select("*").execute()
    return response.data