from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.models import ItemDB
from app.database import SessionLocal, init_db
from app import schemas
from app.crud import create_item, get_item, get_items, update_item, delete_item

app = FastAPI()

# Initialiser la base de données
init_db()

# Dépendance pour obtenir la session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.post("/items", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item_endpoint(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return create_item(db=db, item=item)

@app.get("/items", response_model=list[schemas.ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item_endpoint(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = update_item(db=db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    db_item = delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return None