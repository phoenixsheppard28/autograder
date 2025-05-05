from fastapi import Request
from supabase import create_async_client, AsyncClient

def db_client_get(request:Request) -> AsyncClient:
    return request.app.state.supabase
