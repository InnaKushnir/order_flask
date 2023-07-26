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

from models import Product, Address, Order, OrderStatus, SubAddress


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


@app.route("/products/", methods=["GET"])
def get_objects():
    with get_db() as db:
        products = services.get_all_products(db)
        products_dicts = [{"id": prod.id, "name": prod.name, "color": prod.color, "weight": prod.weight, "price": prod.price} for prod in products]
        return products_dicts


@app.route("/products/<int:product_id>/", methods=["GET"])
def get_object_by_id(product_id: int):
    with get_db() as db:
        prod = services.get_product_by_id(db, product_id)
        if prod is None:
            return {"error": "Object not found"}, 404
        product_dict = {"id": prod.id, "name": prod.name, "color": prod.color, "weight": prod.weight, "price": prod.price}
        return product_dict


@app.post("/products/")
def create_object_route():
    with get_db() as db:
        prod_data = request.get_json()

        try:
            product_create = schemas.ProductCreate(**prod_data)
        except ValueError as e:
            return jsonify({"error": "Invalid data format"}), 400

        new_product = services.product_create(db, product_create)

        serialized_product = {
            "id": new_product.id,
            "name": new_product.name,
            "color": new_product.color,
            "weight": new_product.weight,
            "price": new_product.price
        }

        return jsonify(serialized_product)


if __name__ == '__main__':
    app.run()
