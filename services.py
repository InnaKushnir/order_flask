from sqlalchemy.orm import Session

import models
from models import Object
from schemas import ObjectCreate
import schemas


def get_all_objects(db: Session):
    return db.query(models.Object).all()


def get_object_by_id(db: Session, object_id: int):
    return db.query(models.Object).filter(models.Object.id == object_id).first()


def object_create(db: Session, obj: schemas.ObjectCreate):
    db_object = models.Object(
        name=obj.name,
        color=obj.color,
        weight=obj.weight,
        price=obj.price,
    )
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

