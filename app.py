import os
import dotenv
from flask import Flask
from create_db import db
from models.user import User
from models.offer import Offer
from models.order import Order

app = Flask(__name__)

dotenv.load_dotenv(override=True)

if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('./config/development.py')
else:
    app.config.from_pyfile('./config/production.py')

db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()
