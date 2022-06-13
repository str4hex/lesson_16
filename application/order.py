import datetime

from flask import Blueprint, jsonify, request

from create_db import db
from models.order import Order

order = Blueprint("order", __name__)


@order.route("/",methods=["GET", "POST"])
def order_all_page():
    from app import app
    if request.method == "GET":
        query = Order.query.all()
        order_all = []

        for orders_all in query:
            order_all.append({
                "id": f"{orders_all.id}",
                "name": f"{orders_all.name}",
                "description": f"{orders_all.description}",
                "start_date": f"{orders_all.start_date}",
                "end_date": f"{orders_all.end_date}",
                "address": f"{orders_all.address}",
                "price": f"{orders_all.price}",
                "customer_id": f"{orders_all.customer_id}",
                "executor_id": f"{orders_all.executor_id}",
            })
        return jsonify(order_all)
    elif request.method == "POST":
        data = request.get_json()
        name = data['name']
        description = data['description']
        start_date = data['start_date'].split("/")
        end_date = data['end_date'].split("/")
        address = data['address']
        price = data['price']
        customer_id = data['customer_id']
        executor_id = data['executor_id']
        order_add = Order(name=name,description=description,start_date=datetime.date(int(start_date[2]),
                          int(start_date[0]),int(start_date[1])),end_date=datetime.date(int(end_date[2]),
                          int(end_date[0]),int(end_date[1])),address=address,
                          price=price,customer_id=customer_id,executor_id=executor_id)
        try:
            with app.app_context():
                db.session.add(order_add)
                db.session.commit()
                return {"message": "add new order"}
        except:
            return {"message":"error add new order"}


@order.route("/<int:order_id>", methods=["GET", "PUT","DELETE"])
def order_page(order_id):
    from app import app
    if request.method == "GET":
        query = Order.query.filter_by(id=order_id).first()
        try:
            data = {
                "id": f"{query.id}",
                "name": f"{query.name}",
                "description": f"{query.description}",
                "start_date": f"{query.start_date}",
                "end_date": f"{query.end_date}",
                "address": f"{query.address}",
                "price": f"{query.price}",
                "customer_id": f"{query.customer_id}",
                "executor_id": f"{query.executor_id}",
            }
        except:
            data = {"message":"no order id"}
        return jsonify(data)

    if request.method == "PUT":
        data = request.get_json()
        name = data['name']
        description = data['description']
        start_date = data['start_date'].split("/")
        end_date = data['end_date'].split("/")
        address = data['address']
        price = data['price']
        customer_id = data['customer_id']
        executor_id = data['executor_id']
        try:
            with app.app_context():
                db.session.query(Order).filter_by(id=order_id).update({Order.name:name,
                                                                       Order.description:description,
                                                                       Order.start_date:datetime.date(int(start_date[2]),
                                                                       int(start_date[0]),int(start_date[1])),
                                                                       Order.end_date:datetime.date(int(end_date[2]),
                                                                       int(end_date[0]),int(end_date[1])),
                                                                       Order.address:address,
                                                                       Order.price:price,
                                                                       Order.customer_id:customer_id,
                                                                       Order.executor_id:executor_id})
                db.session.commit()
            return {"message":"order update successful"}
        except:
            return {"message":"order update error"}