import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from main import app


def test_api_register_short_password():
    client = TestClient(app)
    response = client.post(
        "/usuarios/registro",
        data={"username": "prueba", "email": "test_api@example.com", "password": "12"},
    )
    assert response.status_code == 400
    assert response.json().get("detail") == "La contraseña debe tener al menos 8 caracteres"


def test_web_register_short_password_redirect():
    client = TestClient(app)
    response = client.post(
        "/registro",
        data={"nombre": "A", "apellido": "B", "email": "test_web@example.com", "password": "12"},
    )
    # TestClient sigue redirecciones; la URL final debe contener el parámetro de error
    assert response.status_code == 200
    assert "/registro?error=pass_corta" in str(response.url)
