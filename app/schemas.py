from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    name: str
    price: float
    in_stock: bool = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class ItemResponse(ItemBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
