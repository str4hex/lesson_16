import json
from create_db import db
from app import app
from models.user import User
from models.offer import Offer
from models.order import Order

Users = "./json/Users.json"
Orders = "./json/Orders.json"
Offers = "./json/Offers.json"


class Write_db():

    def __init__(self, path):
        self.path = path

    def open_file(self):
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            load_json_file = json.load(file)
            for element in range(len(load_json_file)):
                element_list = load_json_file[element]

                result = json.dumps(element_list).replace(":","=").replace('"',"").replace("{","").replace("}","").\
                    replace("=","='").replace(",","',").replace(" ","").replace("'",'"')
            with app.app_context():
                users = User(id=1, first_name="Hudson", last_name="Pauloh", age=31, email="elliot16@mymail.com",
                             role="customer", phone="6197021684", )
                db.session.add(users)
                db.session.commit()

open_files = Write_db(Users)
open_files.open_file()

"""with app.app_context():
    users = User(id=1, first_name="Hudson", last_name="Pauloh", age=31, email="elliot16@mymail.com",
                 role="customer", phone="6197021684",)
    db.session.add(users)
    db.session.commit()"""
