def test_create_item(client):
    response = client.post(
        "/items", 
        json={"name": "Test Item", "price": 9.99, "in_stock": True}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["price"] == 9.99
    assert data["in_stock"] is True
    assert "id" in data

def test_get_item(client):
    # Créer un item d'abord
    create_response = client.post(
        "/items", 
        json={"name": "Test Get", "price": 5.99, "in_stock": False}
    )
    item_id = create_response.json()["id"]
    
    # Test pour récupérer l'item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Test Get"

def test_update_item(client):
    # Créer un item
    create_response = client.post(
        "/items", 
        json={"name": "To Update", "price": 1.99, "in_stock": True}
    )
    item_id = create_response.json()["id"]
    
    # Mettre à jour l'item
    update_response = client.put(
        f"/items/{item_id}", 
        json={"name": "Updated", "price": 2.99, "in_stock": False}
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["name"] == "Updated"
    assert data["price"] == 2.99
    assert data["in_stock"] is False