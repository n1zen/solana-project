# FastAPI backend app

from fastapi import FastAPI, Request, HTTPException, status

from schemas import(
    ProductCreate,
    ProductResponse
)

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

# create a new product
@app.post("/api/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(product: ProductCreate):
    new_id = max(p["id"] for p in products) + 1 if products else 1
    new_product = {
        "id": new_id,
        "sku": product.sku,
        "name": product.name,
        "category": product.category,
        "price": product.price
    }
    products.append(new_product)
    return new_product

# get all products
@app.get("/api/products", response_model=list[ProductResponse])
def get_all_products():
    return products

# get product by id
@app.get("/api/products/id/{product_id}", response_model=ProductResponse)
def get_product_by_ID(product_id: int):
    for product in products:
        if product.get("id") == product_id:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )

# get product by sku
@app.get("/api/products/sku/{product_sku}", response_model=ProductResponse)
def get_product_by_SKU(product_sku: int):
    for product in products:
        if product.get("sku") == product_sku:
            return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )