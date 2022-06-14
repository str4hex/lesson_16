from flask import Blueprint, jsonify, request

from create_db import db
from models.offer import Offer

offer = Blueprint("offer", __name__)


@offer.route("/", methods=["GET", "POST"])
def offer_all_page():
    from app import app
    if request.method == "GET":
        query = Offer.query.all()
        offer_all = []

        for offers_all in query:
            offer_all.append({
                "id": f"{offers_all.id}",
                "order_id": f"{offers_all.order_id}",
                "executor_id": f"{offers_all.executor_id}",
            })

        return jsonify(offer_all)

    elif request.method == "POST":
        data = request.get_json()
        order_id = data['order_id']
        executor_id = data['executor_id']
        add_offer = Offer(order_id=order_id, executor_id=executor_id)
        try:
            with app.app_context():
                db.session.add(add_offer)
                db.session.commit()
                return {"message": "add offers successful"}
        except:

            return {"message": "add offers error"}


@offer.route("/<int:offer_id>", methods=["GET", "PUT", "DELETE"])
def offer_page(offer_id):
    from app import app
    if request.method == "GET":
        query = Offer.query.filter_by(id=offer_id).first()
        try:
            data = {
                "id": f"{query.id}",
                "order_id": f"{query.order_id}",
                "executor_id": f"{query.executor_id}",
            }
        except:
            data = {
                "message": "no offer id"
            }
        return jsonify(data)

    elif request.method == "PUT":
        data = request.get_json()
        order_id = data['order_id']
        executor_id = data['executor_id']
        try:
            with app.app_context():
                db.session.query(Offer).filter_by(id=offer_id).update({Offer.order_id: order_id,
                                                                       Offer.executor_id: executor_id})
                db.session.commit()

                return {"message": "offers uptade successful"}
        except:
            return {"message": "offers uptade error"}

    elif request.method == "DELETE":
        offers_delete = Offer.query.get(offer_id)
        try:
            with app.app_context():
                db.session.delete(offers_delete)
                db.session.commit()
                return {"message": "Offers delete successful"}
        except:
            return {"message": "Offers delete error"}
