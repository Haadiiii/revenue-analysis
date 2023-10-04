from pydantic import BaseModel

class SaleCreate(BaseModel):
    product_id: int
    quantity: int
    sale_date: str

class SaleResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    sale_date: str