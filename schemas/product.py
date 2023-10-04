from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    inventory: int


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    inventory: int


