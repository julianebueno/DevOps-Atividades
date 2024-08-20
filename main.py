from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()
con = sqlite3.connect("itemsDatabase.db")
cur = con.cursor()

# cur.execute("DROP TABLE IF EXISTS items")
cur.execute("CREATE TABLE IF NOT EXISTS items(name, price, is_offer)")
cur.execute("""
    INSERT INTO items VALUES
        ('Bola', 3, true),
        ('Dado', 5, false),
        ('Cubo', 10, true),
        ('Piramide', 7, false)
""")
con.commit()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items")
async def read_items():
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}