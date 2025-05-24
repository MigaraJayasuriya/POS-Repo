from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    description: str
    supplier: str
    buying_price: float
    selling_price: float
    quantity: int
    created_by: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    date_created: datetime
    date_updated: Optional[datetime] # Null if not updated yet

    class Config:
        orm_model = True