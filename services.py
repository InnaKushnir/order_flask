from sqlalchemy.orm import Session

import models
import schemas


def get_all_products(db: Session):
    return db.query(models.Product).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def product_create(db: Session, obj: schemas.ProductCreate):
    db_product = models.Product(
        name=obj.name,
        color=obj.color,
        weight=obj.weight,
        price=obj.price,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
