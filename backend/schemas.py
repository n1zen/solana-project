# schemas for everything
from typing import Annotated
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class ProductBase(BaseModel):
    sku: int
    name: str = Field(min_length=1, max_length=100)
    category: str = Field(min_length=1, max_length=100)
    price: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

class ProductUpdate(BaseModel):
    sku: int | None = Field(default=None)
    name: str | None = Field(default=None, min_length=1, max_length=100)
    category: str | None = Field(default=None, min_length=1, max_length=100)
    price: int | None = Field(default=None)
class InventoryItemBase(BaseModel):
    quantity: int
    details: str | None = Field(default=None, min_length=1)

class InventoryItemCreate(InventoryItemBase):
    product_id: int

class InventoryItemResponse(InventoryItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_updated: datetime
    product: ProductResponse

class InventoryItemUpdate(BaseModel):
    quantity: int | None = Field(default=None)
    details: Annotated[str | None, Field(min_length=1)] = None
    product_id: int | None = Field(default=None)