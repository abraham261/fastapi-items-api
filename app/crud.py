from sqlalchemy.orm import Session
from app.models import ItemDB
from app.schemas import ItemCreate, ItemUpdate

def create_item(db: Session, item: ItemCreate):
    db_item = ItemDB(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ItemDB).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(ItemDB).filter(ItemDB.id == item_id).first()

def update_item(db: Session, item_id: int, item: ItemUpdate):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if db_item:
        item_data = item.model_dump(exclude_unset=True)
        for key, value in item_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item