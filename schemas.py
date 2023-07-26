
from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    name: str
    color: str
    weight: int
    price: int

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
