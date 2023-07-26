
from pydantic import BaseModel


class ObjectBase(BaseModel):
    id: int
    name: str
    color: str
    weight: int
    price: int

    class Config:
        orm_mode = True


class ObjectCreate(ObjectBase):
    pass


class Object(ObjectBase):
    id: int

    class Config:
        orm_mode = True
