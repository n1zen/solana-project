# models for database (tables)

from __future__ import annotations

from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from schemas import Role

# this is the table for Users
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    email: Mapped[str]= mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(200), nullable=False)
    role: Mapped[str] = mapped_column(SAEnum(Role), default=Role.user)

# this is the table for Products
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sku: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    price: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)

    inventory: Mapped[list[InventoryItem]] = relationship(back_populates="product", cascade="all, delete-orphan",)

# this is the table for InventoryItems
class InventoryItem(Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    quantity: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
    details: Mapped[str | None] = mapped_column(Text, nullable=True, default=None)
    date_updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )

    product: Mapped[Product] = relationship(back_populates="inventory")

# class Order(Base):
#     __tablename__ = "orders"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

# class OrderDetail(Base):
#     __tablename__ = "orderdetails"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)