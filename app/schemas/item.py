# app/schemas/item.py
from pydantic import BaseModel
from typing import Optional


# Schema for creating a new item
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# Schema for an item with an ID
class Item(ItemCreate):
    id: int
