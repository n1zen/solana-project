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

# create order with items
@router.post("/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_order(order: OrderCreate, db: Annotated[AsyncSession, Depends(get_db)]):

    # validate if cashier/user exists
    result = await db.execute(
        select(models.User)
        .where(models.User.id == order.cashier_id)
    )
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This cashier does not exist"
        )
    
    # validate if order number already exists
    result = await db.execute(
        select(models.Order)
        .where(models.Order.order_number == order.order_number)
    )
    existing_order = result.scalars().first()
    if existing_order:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Order number already exists"
        )
    
    new_order_items: list[models.OrderItem] = []
    
    # validate items in OrderItems
    for order_item in order.order_items:
        # get the order_item in inventory if it exists
        result = await db.execute(
            select(models.InventoryItem)
            .options(selectinload(models.InventoryItem.product))
            .where(models.InventoryItem.id == order_item.inventory_item_id)
        )
        item = result.scalars().first()
        # check if it exists
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This item does not exist",
            )
        # check if there is enough items available
        if item.quantity < order_item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There is not enough stock available",
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
    
    new_order = models.Order(
        order_number = order.order_number,
        payment_method = order.payment_method,
        customer_name = order.customer_name,
        cashier_id = order.cashier_id,
        order_items = new_order_items,
        order_status = OrderStatus.pending
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