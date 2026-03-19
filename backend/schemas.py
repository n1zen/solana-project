# schemas for everything
from typing import Annotated
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, EmailStr, Field

class Role(str, Enum):
    admin = "admin"
    user = "user"

class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=120)
    lastname: str = Field(min_length=1, max_length=120)
    firstname: str = Field(min_length=1, max_length=120)
    email: EmailStr = Field(max_length=120)
    role: Role = Field(default=Role.user)

class UserCreate(UserBase):
    password: str = Field(min_length=8) 

class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    lastname: str
    firstname: str
    role: Role

class UserPrivate(UserPublic):
    email: EmailStr

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=120)
    firstname: str | None = Field(default=None, min_length=1, max_length=120)
    lastname: str | None = Field(default=None, min_length=1, max_length=120)
    role: Role | None = Field(default=Role.user)

class Token(BaseModel):
    access_token: str
    token_type: str

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