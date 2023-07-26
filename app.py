import os
from typing import List

from flask import Flask, g, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import Session

import schemas
import services
from database import SessionLocal

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://user:password@localhost/db_object"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Object, Address, Order, OrderStatus, SubAddress


def get_db():
    if 'db' not in g:
        g.db = SessionLocal()

    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/objects/", methods=["GET"])
def get_objects():
    with get_db() as db:
        objects = services.get_all_objects(db)
        object_dicts = [{"id": obj.id, "name": obj.name, "color": obj.color, "weight": obj.weight, "price": obj.price} for obj in objects]
        return object_dicts


@app.route("/objects/<int:object_id>/", methods=["GET"])
def get_object_by_id(object_id: int):
    with get_db() as db:
        obj = services.get_object_by_id(db, object_id)
        if obj is None:
            return {"error": "Object not found"}, 404
        object_dict = {"id": obj.id, "name": obj.name, "color": obj.color, "weight": obj.weight, "price": obj.price}
        return object_dict


@app.post("/objects/")
def create_object_route():
    with get_db() as db:
        obj_data = request.get_json()

        try:
            obj_create = schemas.ObjectCreate(**obj_data)
        except ValueError as e:
            return jsonify({"error": "Invalid data format"}), 400

        new_object = services.object_create(db, obj_create)

        serialized_object = {
            "id": new_object.id,
            "name": new_object.name,
            "color": new_object.color,
            "weight": new_object.weight,
            "price": new_object.price
        }

        return jsonify(serialized_object)


if __name__ == '__main__':
    app.run()
