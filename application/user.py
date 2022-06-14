from create_db import db
from flask import Blueprint, jsonify, request
from models.user import User

user = Blueprint("user", __name__)


@user.route("/", methods=["GET", "POST"])
def user_all_page():
    from app import app
    if request.method == "GET":
        query = User.query.all()
        users_all = []
        for user_all in query:
            print(user_all.id)
            users_all.append({
                "id": f"{user_all.id}",
                "first_name": f"{user_all.first_name}",
                "last_name": f"{user_all.last_name}",
                "age": f"{user_all.age}",
                "email": f"{user_all.email}",
                "role": f"{user_all.role}",
                "phone": f"{user_all.phone}",
            })
        return jsonify(users_all)

    elif request.method == "POST":
        data = request.get_json()
        first_name = data['first_name']
        last_name = data['last_name']
        age = data['age']
        email = data['email']
        role = data['role']
        phone = data['phone']
        add_user = User(first_name=first_name, last_name=last_name, age=age, email=email, role=role, phone=phone)
        try:
            with app.app_context():
                db.session.add(add_user)
                db.session.commit()
            return {"message": "add user successful"}
        except:
            return {"messsage":"error"}


@user.route("/<int:id_user>", methods=["GET", "PUT", "PUT", "DELETE"])
def user_page(id_user):
    from app import app
    if request.method == "GET":
        query = User.query.filter_by(id=id_user).first()
        try:
            data = {
                "id": f"{query.id}",
                "first_name": f"{query.first_name}",
                "last_name": f"{query.last_name}",
                "age": f"{query.age}",
                "email": f"{query.email}",
                "role": f"{query.role}",
                "phone": f"{query.phone}",
            }
        except:
            data = {"message": "no user id"}
        return jsonify(data)

    elif request.method == "PUT":
        data = request.get_json()
        first_name = data['first_name']
        last_name = data['last_name']
        age = data['age']
        email = data['email']
        role = data['role']
        phone = data['phone']
        try:
            with app.app_context():
                db.session.query(User).filter_by(id=id_user).update({User.first_name: first_name,
                                                                     User.last_name: last_name,
                                                                     User.age: age,
                                                                     User.email: email,
                                                                     User.role: role,
                                                                     User.phone: phone})
                db.session.commit()
                return {"message": "user update successful"}
        except:
            return {"message": "error"}

    elif request.method == "DELETE":
        query = User.query.get(id_user)
        try:
            with app.app_context():
                db.session.delete(query)
                db.session.commit()
            return {"message": "user delete successful"}
        except:
            return {"message":"error"}