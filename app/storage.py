# app/storage.py
from typing import Dict, List
from app.schemas.item import Item, ItemCreate

# Store items in memory
items_db: Dict[int, Item] = {}
next_id = 1

def get_items() -> List[Item]:
    return list(items_db.values())

def get_item(item_id: int) -> Item | None:
    return items_db.get(item_id)

def create_item(item_data: ItemCreate) -> Item:
    global next_id
    item = Item(id=next_id, **item_data.dict())
    items_db[next_id] = item
    next_id += 1
    return item

def delete_item(item_id: int) -> bool:
    return items_db.pop(item_id, None) is not None
