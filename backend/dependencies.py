# some reusable helper functions

from fastapi import HTTPException, status
from sqlalchemy import select

import models

# check if the product already exists in the database
# throw an exception if it does
def product_exist(item: str, content: str, db):
    if item == "sku":
        result = db.execute(
            select(models.Product).where(models.Product.sku == content)
        )
        message = "Product SKU already exists."
    elif item == "name":
        result = db.execute(
            select(models.Product).where(models.Product.name == content)
        )
        message = "Product NAME already exists."
    
    existing_item = result.scalars().first()

    if existing_item:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )