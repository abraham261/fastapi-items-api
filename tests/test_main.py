import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app import models

client = TestClient(app)

@pytest.fixture
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def create_item(db):
    item_data = {"name": "Test Item", "price": 10.5, "in_stock": True}
    new_item = models.ItemDB(**item_data)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def test_create_item(create_item):
    assert create_item.name == "Test Item"
    assert create_item.price == 10.5
    assert create_item.in_stock is True

def test_read_items(client):  # Ajoutez la fixture client
    response = client.get("/items")
    assert response.status_code == 200

def test_read_item(create_item):
    response = client.get(f"/items/{create_item.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == create_item.name
