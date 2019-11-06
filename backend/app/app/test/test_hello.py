# test_hello.py
import sys

sys.path.append("../app/")
from app.main import app

def test_hello():
    response = app.test_client().get('/api/')

    assert response.status_code == 200
    assert response.data == b'{"message":"Hello World"}\n'
