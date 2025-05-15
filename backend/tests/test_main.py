from fastapi.testclient import TestClient
from app.main import app
import uuid
from datetime import datetime
import json




client =TestClient(app)

def test_example():
     with TestClient(app) as client:
        ts = datetime.now()
        log = {
            # "submission_id":str(uuid.uuid4()),
            "log":None,
            # "created_at": str(ts)
         }
        
        r = client.post("/log",json=log)
        assert r.status_code == 200
        print(r.text)
      