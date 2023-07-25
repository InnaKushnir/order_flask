from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from database import Base


class Object(Base):
    __tablename__ = "object"

    id = Column(Integer, primary_key=True, index=True)
    color = Column(String(255), nullable=False)
    weight = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    street = Column(String(255), nullable=False)

    orders = relationship("Order", back_populates="address")


class OrderStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    status = Column(String(length=50), nullable=False, default=OrderStatus.PENDING.value)

    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address", back_populates="orders")

