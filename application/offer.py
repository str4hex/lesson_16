from flask import Blueprint, jsonify
from models.offer import Offer

offer = Blueprint("offer", __name__)


@offer.route("/")
def offer_all_page():
    query = Offer.query.all()
    offer_all = []

    for offers_all in query:
        offer_all.append({
            "id": f"{offers_all.id}",
            "order_id": f"{offers_all.order_id}",
            "executor_id": f"{offers_all.executor_id}",
        })

    return jsonify(offer_all)


@offer.route("/<int:offer_id>")
def offer_page(offer_id):
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
