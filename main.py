# Create the basic routes
# Cteaye the database connection
# Create the models 
# Connect the models to the routes
# Perform database functions iwth routes

from fastapi import FastAPI, HTTPException, status, Query, Response
from pydantic import BaseModel
from typing import Optional, List
from random import randrange

app = FastAPI()

class Item(BaseModel):
    name: str
    buyingprice: float
    sellingprice: float
    quantity: int
    producedby: str
    size: str
    color: str
    description: str
    category: str
    createdby: str
    datecreated: str
    dateupdated: str
    
items = []

@app.get("/items", response_model=List[Item])
async def get_items():
    return items

@app.post("/items", response_model = Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model = Item)
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    del items[item_id]
    return {"message": "Item deleted successfully"}
