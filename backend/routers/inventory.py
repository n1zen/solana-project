# routes/endpoints for products
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import models
from database import get_db
from schemas import (
    InventoryItemCreate,
    InventoryItemResponse,
    InventoryItemUpdate
)

router = APIRouter()

# create inventory item
@router.post("/",
        response_model=InventoryItemResponse,
        status_code=status.HTTP_201_CREATED)
async def create_inventory_item(inventory_item: InventoryItemCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    new_inventory_item = models.InventoryItem(
        product_id = inventory_item.product_id,
        quantity = inventory_item.quantity,
        details = inventory_item.details,
    )

    db.add(new_inventory_item)
    await db.commit()
    await db.refresh(new_inventory_item, attribute_names=["product"])
    return new_inventory_item

# get all inventoryitems
@router.get("/", response_model=list[InventoryItemResponse])
async def get_inventory(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.InventoryItem).options(selectinload(models.InventoryItem.product))
    )
    inventory = result.scalars().all()
    return inventory

# get inventoryitem by id
@router.get("/{inventory_id}", response_model=InventoryItemResponse)
async def get_inventory_item(inventory_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.InventoryItem).options(selectinload(models.InventoryItem.product))
        .where(models.InventoryItem.id == inventory_id)
    )
    item = result.scalars().first()
    if item:
        return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Inventory of item not found."
    )

# update inventory item
@router.patch("/{inventory_id}", response_model=InventoryItemResponse)
async def update_inventory_item(inventory_id: int, item_update: InventoryItemUpdate, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.InventoryItem).options(selectinload(models.InventoryItem.product))
        .where(models.InventoryItem.id == inventory_id)
    )
    item = result.scalars().first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory of item not found."
        )
    if item_update.quantity is not None:
        item.quantity = item_update.quantity
    if item_update.details is not None:
        item.details = item_update.details
    if item_update.product_id is not None:
        item.product_id = item_update.product_id

    await db.commit()
    await db.refresh(item, attribute_names=["product"])
    return item

# delete inventory item
@router.delete("/{inventory_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inventory_item(inventory_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.InventoryItem).where(models.InventoryItem.id == inventory_id)
    )
    item = result.scalars().first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory of item not found."
        )
    
    await db.delete(item)
    await db.commit()