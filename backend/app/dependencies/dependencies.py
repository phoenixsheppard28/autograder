from fastapi import Request
from supabase import AsyncClient

def db_client_get(request:Request) -> AsyncClient:
    return request.app.state.supabase
