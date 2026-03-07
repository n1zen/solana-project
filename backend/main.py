# FastAPI backend app
from typing import Annotated

from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_db
from schemas import(
    ProductCreate,
    ProductResponse,
    ProductUpdate,
    InventoryItemCreate,
    InventoryItemResponse,
    InventoryItemUpdate
)
from dependencies import product_exist

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return { "message": "hello world" }

# create a new product
@app.post("/api/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(product: ProductCreate, db: Annotated[Session, Depends(get_db)]):
    
    product_exist("sku", product.sku, db)
    product_exist("name", product.name, db)
    
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

# update product using patch
@app.patch("/api/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_update: ProductUpdate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(models.Product).where(models.Product.id == product_id)
    )
    product = result.scalars().first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    if product_update.sku is not None and product_update.sku != product.sku:
        product_exist("sku", product_update.sku, db)
    
    if product_update.name is not None and product_update.name != product.name:
        product_exist("name", product_update.name, db)

    if product_update.sku is not None:
        product.sku = product_update.sku
    if product_update.name is not None:
        product.name = product_update.name
    if product_update.category is not None:
        product.category = product_update.category
    if product_update.price is not None:
        product.price = product_update.price
    
    db.commit()
    db.refresh(product)
    return product

# delete product
@app.delete("/api/product/{product_id}",
            status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(models.Product).where(models.Product.id == product_id)
    )
    product = result.scalars().first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    db.delete(product)
    db.commit()

# create inventory item
@app.post("/api/inventory",
        response_model=InventoryItemResponse,
        status_code=status.HTTP_201_CREATED)
def create_inventory_item(inventory_item: InventoryItemCreate, db: Annotated[Session, Depends(get_db)]):
    new_inventory_item = models.InventoryItem(
        product_id = inventory_item.product_id,
        quantity = inventory_item.quantity,
        details = inventory_item.details,
    )

    db.add(new_inventory_item)
    db.commit()
    db.refresh(new_inventory_item)
    return new_inventory_item

# get all inventoryitems
@app.get("/api/inventory", response_model=list[InventoryItemResponse])
def get_inventory(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(models.InventoryItem)
    )
    inventory = result.scalars().all()
    return inventory

# get inventoryitem by id
@app.get("/api/inventory/{inventory_id}", response_model=InventoryItemResponse)
def get_inventory_item(inventory_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(models.InventoryItem).where(models.InventoryItem.id == inventory_id)
    )
    item = result.scalars().first()
    if item:
        return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Inventory of item not found."
    )

# update inventory item
@app.patch("/api/inventory/{inventory_id}", response_model=InventoryItemResponse)
def update_inventory_item(inventory_id: int, item_update: InventoryItemUpdate, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(models.InventoryItem).where(models.InventoryItem.id == inventory_id)
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

    db.commit()
    db.refresh(item)
    return item

# delete inventory item
@app.delete("/api/inventory/{inventory_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inventory_item(inventory_id: int, db: Annotated[Session, Depends(get_db)]):
    result = db.execute(
        select(models.InventoryItem).where(models.InventoryItem.id == inventory_id)
    )
    item = result.scalars().first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory of item not found."
        )
    
    db.delete(item)
    db.commit()