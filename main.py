''' API de controle de itens '''

import sqlite3
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
con = sqlite3.connect("itemsDatabase.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS items(name, price, is_offer)")
cur.execute("SELECT * FROM items")
itemsDB = cur.fetchall()
if itemsDB is None:
    cur.execute("""
        INSERT INTO items VALUES
            ('Bola', 3, true),
            ('Dado', 5, false),
            ('Cubo', 10, true),
            ('Piramide', 7, false)
    """)
    con.commit()

''' Classe Item '''

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

''' Rotas '''

@app.get("/")
async def read_root():
    return {"message": "Api de controle de itens"}

''' GET TODOS OS ITEM '''

@app.get("/items")
async def read_items():
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    if items is None:
        return {"message": "Nenhum item encontrado"}
    return items

''' GET ITEM POR ID '''

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    cur.execute("SELECT * FROM items WHERE rowid = ?", (item_id,))
    item = cur.fetchone()
    if item is None:
        return {"message": "Item não encontrado"}
    return item

''' POST ITEM '''

@app.post("/items")
async def create_item(item: Item):
    cur.execute("INSERT INTO items VALUES (?, ?, ?)", (item.name, item.price, item.is_offer))
    con.commit()
    if cur.rowcount == 0:
        return {"message": "Erro ao inserir item"}
    return item

''' PUT ITEM POR ID '''

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    cur.execute("UPDATE items SET name = ?, price = ?, is_offer = ? WHERE rowid = ?" ,
                (item.name, item.price, item.is_offer, item_id))
    con.commit()
    return item

''' DELETE ITEM POR ID '''

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    cur.execute("DELETE FROM items WHERE rowid = ?", (item_id,))
    con.commit()
    if cur.rowcount == 0:
        return {"message": "Item não encontrado"}
    return {"message": "Item deletado"}
