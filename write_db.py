import json
from create_db import db
from app import app
from models.user import User
from models.offer import Offer
from models.order import Order
import datetime

Users = "./json/Users.json"
Orders = "./json/Orders.json"
Offers = "./json/Offers.json"

with open(Users, "r", encoding="utf-8") as json_user:
    load_json = json.load(json_user)
    for loads in load_json:
        users = User(id=loads["id"], first_name=loads["first_name"], last_name=loads["last_name"], age=loads["age"],
                     email=loads["email"], role=loads["role"], phone=loads["phone"])
        with app.app_context():
            db.session.add(users)
            db.session.commit()
    print(f'{json_user} - добавлено в СУБД')

with open(Orders, "r", encoding="utf-8") as json_user:
    load_json = json.load(json_user)
    for loads in load_json:
        start_dates = loads['start_date'].split("/")
        end_dates = loads['end_date'].split("/")
        users = Order(id=loads["id"], name=loads["name"], description=loads["description"],
                      start_date=datetime.date(int(start_dates[2]),int(start_dates[0]),int(start_dates[1])),
                      end_date = datetime.date(int(end_dates[2]),int(end_dates[0]),int(end_dates[1])), address = loads["address"], price = loads["price"],
                      customer_id = loads["customer_id"], executor_id = loads["executor_id"])

        with app.app_context():
            db.session.add(users)
            db.session.commit()
    print(f'{json_user} - добавлено в СУБД')

with open(Offers, "r", encoding="utf-8") as json_user:
    load_json = json.load(json_user)
    for loads in load_json:
        users = Offer(id=loads["id"], order_id=loads["order_id"], executor_id=loads["executor_id"])
        with app.app_context():
            db.session.add(users)
            db.session.commit()
    print(f'{json_user} - добавлено в СУБД')
