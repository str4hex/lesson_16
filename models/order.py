from create_db import db
from sqlalchemy import DATETIME

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.DATE)
    end_date = db.Column(db.DATE)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer,db.ForeignKey('user.id'))
