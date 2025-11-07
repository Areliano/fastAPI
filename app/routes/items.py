from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.item import Item, ItemCreate
from app import storage

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=List[Item])
def read_items():
    return storage.get_items()

@router.post("/", response_model=Item)
def create_item(item: ItemCreate):
    return storage.create_item(item)

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = storage.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}")
def delete_item(item_id: int):
    deleted = storage.delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
