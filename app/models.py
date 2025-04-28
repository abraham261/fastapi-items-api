from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import declarative_base  # Nouvelle importation

Base = declarative_base()

class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    in_stock = Column(Boolean, default=True)