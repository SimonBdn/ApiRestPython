from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    created_at: datetime

    class Config:
        from_attributes = True
