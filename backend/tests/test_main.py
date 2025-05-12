from fastapi.testclient import TestClient
from app.main import app


client =TestClient(app)

def test_example():
     with TestClient(app) as client:
        r = client.get("/users")
        assert r.status_code == 200