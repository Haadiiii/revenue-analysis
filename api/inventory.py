from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.product import ProductResponse
from typing import List
from models.database import Product
from models.database import SessionLocal

app = APIRouter()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# inventory-low-stock

@app.get("/inventory/low-stock", response_model=List[ProductResponse])
def get_low_stock_inventory(db: Session = Depends(get_db)):
    low_stock_threshold = 10  # Define your low stock threshold here
    low_stock_products = db.query(Product).filter(Product.inventory < low_stock_threshold).all()

    converted_low_stock = []
    for product in low_stock_products:
        try:
            product.inventory = int(product.inventory)
        except ValueError:
            pass  # If conversion to int fails, leave it as is
        converted_low_stock.append(product)

    return converted_low_stock


@app.get("/inventory/{product_id}", response_model=ProductResponse)
def get_inventory(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
