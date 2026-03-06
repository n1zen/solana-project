# schemas for everything
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