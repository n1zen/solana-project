# routes/endpoints for orders
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import models
from database import get_db
from schemas import OrderItemCreate, OrderItemResponse, OrderItemUpdate, OrderCreate, OrderResponse, OrderUpdate, OrderStatus

router = APIRouter()

# check if order does not exists
async def order_does_not_exists(type: str, content: int, db):
    if type == "id":
        result = await db.execute(
            select(models.Order).options(
                selectinload(models.Order.order_items)
                .selectinload(models.OrderItem.inventory_item)
                .selectinload(models.InventoryItem.product),
                selectinload(models.Order.cashier)
            ).where(models.Order.id == content)
        )
    elif type == "number":
        result = await db.execute(
            select(models.Order).options(
                selectinload(models.Order.order_items)
                .selectinload(models.OrderItem.inventory_item)
                .selectinload(models.InventoryItem.product),
                selectinload(models.Order.cashier)
            ).where(models.Order.order_number == content)
        )
    order = result.scalars().first()
    if order:
        return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Order does not exist"
    )

# validate if cashier/user exists
async def cashier_exists(cashier_id: int, db):
    result = await db.execute(
        select(models.User)
        .where(models.User.id == cashier_id)
    )
    user = result.scalars().first()
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="This cashier does not exist"
    )

# validate if order number already exists
async def order_number_exists(order_number: int, db):
    result = await db.execute(
        select(models.Order)
        .where(models.Order.order_number == order_number)
    )
    existing_order = result.scalars().all()
    if existing_order:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This order number already exists"
        )

async def map_inventory(order, db):
    # get all inventory items with their products in order_items
    item_ids = [order_item.inventory_item_id for order_item in order.order_items]
    result = await db.execute(
        select(models.InventoryItem)
        .options(selectinload(models.InventoryItem.product))
        .where(models.InventoryItem.id.in_(item_ids))
    )
    invetory_map = {item.id: item for item in result.scalars().all()}
    return invetory_map

async def validate_order_items(order, db):
    new_order_items: list[models.OrderItem] = []

    # get all inventory items with their products in order_items
    inventory_map = await map_inventory(order, db)

    # validate
    for order_item in order.order_items:
        item = inventory_map.get(order_item.inventory_item_id)

        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This item does not exist"
            )
        
        if item.quantity < order_item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There is not enough items"
            )
        
        item.quantity -= order_item.quantity
        db.add(item)

        new_order_item = models.OrderItem(
            inventory_item_id = order_item.inventory_item_id,
            quantity = order_item.quantity,
            unit_price = item.product.price,
            price_adjustment = order_item.price_adjustment,
            notes = order_item.notes
        )
        new_order_items.append(new_order_item)
    return new_order_items

# create order with items
@router.post("/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_order(order: OrderCreate, db: Annotated[AsyncSession, Depends(get_db)]):

    # validate if cashier/user exists
    await cashier_exists(order.cashier_id, db)
    
    # validate if order number already exists
    await order_number_exists(order.order_number, db)
    
    # validate order_items in order
    new_order_items = await validate_order_items(order, db)

    new_order = models.Order(
        order_number = order.order_number,
        payment_method = order.payment_method,
        customer_name = order.customer_name,
        cashier_id = order.cashier_id,
        order_items = new_order_items,
        order_status = order.order_status
    )
    
    try:
        db.add(new_order)
        await db.commit()
        await db.refresh(new_order, attribute_names=["order_items", "cashier"])
        return new_order
    except Exception:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create order"
        )

# get all orders
@router.get("/", response_model=list[OrderResponse])
async def get_all_orders(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Order).options(
            selectinload(models.Order.order_items)
            .selectinload(models.OrderItem.inventory_item)
            .selectinload(models.InventoryItem.product)
            , selectinload(models.Order.cashier)
        )
    )
    orders = result.scalars().all()
    return orders

# get an order by id
@router.get("/orderid/{order_id}", response_model=OrderResponse)
async def get_order_by_id(order_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    order = await order_does_not_exists("id", order_id, db)
    return order

# get an order by order_number
@router.get("/ordernumber/{order_number}", response_model=OrderResponse)
async def get_order_by_number(order_number: int, db: Annotated[AsyncSession, Depends(get_db)]):
    order = await order_does_not_exists("number", order_number, db)
    return order

# update an order
@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(updated_order: OrderCreate, order_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    # check if order does not exist
    order = await order_does_not_exists("id", order_id, db)

    # validate cashier
    await cashier_exists(updated_order.cashier_id, db)

    # validate order_number if changed
    if updated_order.order_number != order.order_number:
        await order_number_exists(updated_order.order_number, db)
    
    # validate and get order_items
    updated_order_items = await validate_order_items(updated_order, db)

    order.order_number = updated_order.order_number
    order.payment_method = updated_order.payment_method
    order.customer_name = updated_order.customer_name
    order.order_status = updated_order.order_status
    order.cashier_id = updated_order.cashier_id
    order.order_items = updated_order_items

    try:
        await db.commit()
        await db.refresh(order, attribute_names=["order_items", "cashier"])
        return order
    except Exception:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create order"
        )

# delete an order
@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    order = await order_does_not_exists("id", order_id, db)
    await db.delete(order)
    await db.commit()