from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.sales import SaleCreate, SaleResponse
from typing import List
from models.database import Sale
from models.database import SessionLocal
from fastapi import HTTPException


app = APIRouter()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/sales/", response_model=List[SaleResponse])
def read_sales(db: Session = Depends(get_db)):
    sales = db.query(Sale).all()
    return sales

@app.post("/sales/", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    db_sale = Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale


# Update sale

@app.put("/sales/{sale_is}", response_model=SaleResponse)
def sales_update(sale_id: int, sale: SaleCreate, db: Session = Depends(get_db)):
    db_sale = db.query(sale).filter(sale.id == sale_id).first()
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    db_sale.name = sale.name
    db_sale.price = sale.price
    db_sale.description = sale.description
    db.commit()
    db.refresh(db_sale)
    return db_sale



