# schemas for everything
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