from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.product import ProductResponse
from sqlalchemy import func
from datetime import datetime, timedelta
from models.database import Product
from models.database import Sale
from models.database import SessionLocal


app = APIRouter()
# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/revenue/daily", response_model=dict)
def get_daily_revenue(db: Session = Depends(get_db)):
    today = datetime.now().date()
    today_str = today.strftime("%Y-%m-%d")
    print("Today's Date:", today_str)

    daily_revenue = (
        db.query(func.date(Sale.sale_date).label("date"), func.sum(Sale.quantity * Product.price).label("revenue"))
        .filter(func.date(Sale.sale_date) == today_str)
        .group_by(func.date(Sale.sale_date))
        .all()
    )

    result = {item.date: item.revenue for item in daily_revenue}

    return result

# revenue-weekly
@app.get("/revenue/weekly", response_model=dict)
def get_weekly_revenue(db: Session = Depends(get_db)):
    today = datetime.now().date()
    start_date = today - timedelta(days=today.weekday())
    end_date = start_date + timedelta(days=6)

    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    print("Start Date:", start_date_str)
    print("End Date:", end_date_str)

    weekly_revenue = (
        db.query(func.date(Sale.sale_date).label("date"), func.sum(Sale.quantity * Product.price).label("revenue"))
        .filter(func.date(Sale.sale_date) >= start_date_str)
        .filter(func.date(Sale.sale_date) <= end_date_str)
        .group_by(func.date(Sale.sale_date))
        .all()
    )

    result = {item.date: item.revenue for item in weekly_revenue}

    return result

# revenue-monthly
@app.get("/revenue/monthly", response_model=dict)
def get_monthly_revenue(db: Session = Depends(get_db)):
    today = datetime.now().date()
    start_date = today.replace(day=1)
    end_date = start_date + timedelta(days=31)

    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    print("Start Date:", start_date_str)
    print("End Date:", end_date_str)

    monthly_revenue = (
        db.query(func.date(Sale.sale_date).label("date"), func.sum(Sale.quantity * Product.price).label("revenue"))
        .filter(func.date(Sale.sale_date) >= start_date_str)
        .filter(func.date(Sale.sale_date) <= end_date_str)
        .group_by(func.date(Sale.sale_date))
        .all()
    )

    result = {item.date: item.revenue for item in monthly_revenue}

    return result

# revenue-yearly
@app.get("/revenue/yearly", response_model=dict)
def get_yearly_revenue(db: Session = Depends(get_db)):
    today = datetime.now().date()
    start_date = today.replace(month=1, day=1)
    end_date = start_date.replace(month=12, day=31)

    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")

    print("Start Date:", start_date_str)
    print("End Date:", end_date_str)

    yearly_revenue = (
        db.query(func.date(Sale.sale_date).label("date"), func.sum(Sale.quantity * Product.price).label("revenue"))
        .filter(func.date(Sale.sale_date) >= start_date_str)
        .filter(func.date(Sale.sale_date) <= end_date_str)
        .group_by(func.date(Sale.sale_date))
        .all()
    )

    result = {item.date: item.revenue for item in yearly_revenue}

    return result