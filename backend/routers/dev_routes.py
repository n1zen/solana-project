# routes/endpoints for dev tools
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models
from database import get_db

router = APIRouter()

# (dev only) delete inventory
@router.delete("/purge/inventory", status_code=status.HTTP_204_NO_CONTENT)
async def dev_purge_inventory(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.InventoryItem))
    inventory = result.scalars().all()
    if inventory == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory is empty"
        )
    for item in inventory:
        await db.delete(item)
    await db.commit()

# (dev only) delete all products
@router.delete("/purge/products", status_code=status.HTTP_204_NO_CONTENT)
async def dev_purge_products(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(models.Product))
    products = result.scalars().all()
    if products == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No products to delete"
        )
    for product in products:
        await db.delete(product)
    await db.commit()

# (dev only) delete all users
@router.delete(
    '/purge/users',
    status_code=status.HTTP_204_NO_CONTENT
)
async def dev_purge_users(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.User)
    )
    users = result.scalars().all()
    if users == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            details="No users to delete"
        )
    for user in users:
        await db.delete(user)
    await db.commit()

# (dev only) delete all orders
@router.delete(
    '/purge/orders',
    status_code=status.HTTP_204_NO_CONTENT
)
async def dev_purge_orders(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Order)
    )
    orders = result.scalars().all()
    if orders == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            details="No orders to delete"
        )
    for order in orders:
        await db.delete(order)
    await db.commit()
