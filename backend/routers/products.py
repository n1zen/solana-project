# routes/endpoints for products
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models
from database import get_db
from schemas import ProductCreate, ProductResponse, ProductUpdate
from dependencies import product_exist

router = APIRouter()

# create a new product
@router.post("/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(product: ProductCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    
    await product_exist("sku", product.sku, db)
    await product_exist("name", product.name, db)
    
    new_product = models.Product(
        sku = product.sku,
        name = product.name,
        category = product.category,
        price = product.price
    )

    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    
    return new_product

# get all products
@router.get("/", response_model=list[ProductResponse])
async def get_all_products(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Product)
    )
    products = result.scalars().all()
    return products

# get product by id
@router.get("/id/{product_id}", response_model=ProductResponse)
async def get_product_by_ID(product_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Product).where(models.Product.id == product_id)
    )
    product = result.scalars().first()
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )

# get product by sku
@router.get("/sku/{product_sku}", response_model=ProductResponse)
async def get_product_by_SKU(product_sku: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Product).where(models.Product.sku == product_sku)
    )
    product = result.scalars().first()
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )

# update product using patch
@router.patch("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product_update: ProductUpdate, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Product).where(models.Product.id == product_id)
    )
    product = result.scalars().first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    if product_update.sku is not None and product_update.sku != product.sku:
        await product_exist("sku", product_update.sku, db)
    
    if product_update.name is not None and product_update.name != product.name:
        await product_exist("name", product_update.name, db)

    if product_update.sku is not None:
        product.sku = product_update.sku
    if product_update.name is not None:
        product.name = product_update.name
    if product_update.category is not None:
        product.category = product_update.category
    if product_update.price is not None:
        product.price = product_update.price
    
    await db.commit()
    await db.refresh(product)
    return product

# delete product
@router.delete("/{product_id}",
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(
        select(models.Product).where(models.Product.id == product_id)
    )
    product = result.scalars().first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    await db.delete(product)
    await db.commit()