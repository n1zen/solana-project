# some reusable helper functions

from fastapi import HTTPException, status
from sqlalchemy import select, func

import models

# check if the product already exists in the database
# throw an exception if it does
async def product_exist(item: str, content: str, db):
    if item == "sku":
        result = await db.execute(
            select(models.Product).where(models.Product.sku == content)
        )
        message = "Product SKU already exists."
    elif item == "name":
        result = await db.execute(
            select(models.Product).where(models.Product.name == content)
        )
        message = "Product NAME already exists."
    
    existing_item = result.scalars().first()

    if existing_item:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=message
        )
    
async def user_exist(item: str, content: str, db):
    if item == "username":
        result = await db.execute(
            select(models.User)
            .where(
                func.lower(models.User.username) == content.lower()),
        )
        message = "Username is already taken!"
    elif item == "email":
        result = await db.execute(
            select(models.User)
            .where(
                func.lower(models.User.email) == content.lower()
            ),
        )
        message = "Email is already registered!"
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=message
        )