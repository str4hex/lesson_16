import os
import dotenv
from flask import Flask
from create_db import db
from models.user import User
from models.offer import Offer
from models.order import Order
from application.user import user
from application.order import order
from application.offer import offer

app = Flask(__name__)

dotenv.load_dotenv(override=True)

if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('./config/development.py')
else:
    app.config.from_pyfile('./config/production.py')

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(user, url_prefix='/users')
app.register_blueprint(order, url_prefix='/orders')
app.register_blueprint(offer,url_prefix="/offer")


if __name__ == '__main__':
    app.run()
