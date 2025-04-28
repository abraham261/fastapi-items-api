from fastapi.testclient import TestClient
from app.main import app  # Importation correcte de app
from app.database import init_db  # Importation correcte de init_db

client = TestClient(app)

def setup_module():
    init_db()  # Crée les tables avant les tests

def test_create_item():
    response = client.post("/items", json={"name": "Laptop", "price": 999.99, "in_stock": True})
    assert response.status_code == 201
    assert response.json()["name"] == "Laptop"

def test_get_item():
    # Crée un item d'abord
    client.post("/items", json={"name": "Phone", "price": 599.99, "in_stock": True})
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
