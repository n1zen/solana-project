# FastAPI backend app

from fastapi import FastAPI, Request, HTTPException, status

app = FastAPI()

products: list[dict] = [
    {
        "id": 1,
        "sku": 250001,
        "name": "Cat in Box",
        "category": "Animals",
        "price": 100,
    },
    {
        "id": 2,
        "sku": 240005,
        "name": "Base 1-slot",
        "category": "Bases",
        "price": 70,
    },
]

@app.get("/")
def home():
    return { "message": "hello world" }

# get all products
@app.get("/api/products")
def get_all_products():
    return products

# get product by id
@app.get("/api/products/id/{product_id}")
def get_product_by_ID(product_id: int):
    for product in products:
        if product.get("id") == product_id:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )

# get product by sku
@app.get("/api/products/sku/{product_sku}")
def get_product_by_SKU(product_sku: int):
    for product in products:
        if product.get("sku") == product_sku:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )