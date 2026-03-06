# FastAPI backend app
from typing import Annotated

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_db
from schemas import(
    ProductCreate,
    ProductResponse,
    InventoryItemCreate,
    InventoryItemResponse
)
from dependencies import does_exist

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return { "message": "hello world" }

# create a new product
@app.post("/api/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(product: ProductCreate, db: Annotated[Session, Depends(get_db)]):
    
    does_exist("sku", product.sku, db)
    does_exist("name", product.name, db)
    
    new_product = models.Product(
        sku = product.sku,
        name = product.name,
        category = product.category,
        price = product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product

# get all products
@app.get("/api/products", response_model=list[ProductResponse])
def get_all_products(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(models.Product)
    )
    products = result.scalars().all()
    return products

# get product by id
@app.get("/api/products/id/{product_id}", response_model=ProductResponse)
def get_product_by_ID(product_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
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
@app.get("/api/products/sku/{product_sku}", response_model=ProductResponse)
def get_product_by_SKU(product_sku: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(models.Product).where(models.Product.sku == product_sku)
    )
    product = result.scalars().first()
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )