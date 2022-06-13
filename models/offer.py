from create_db import db


class Offer(db.Model):
    __tablenaame__ = 'offer'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    order_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer,db.ForeignKey('user.id'))

