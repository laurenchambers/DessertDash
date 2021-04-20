
from flask import Blueprint, jsonify, session, request
from flask_login import login_required
from app.models import db, User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}


@user_routes.route('/<int:id>/')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/edit-user/<int:id>/', methods=["POST"])
@login_required
def edit_user(id):
    req = request.get_json()
    print('req!!', req)
    user = User.query.get(id)
    user.id = req['id']
    user.address = req['address']
    user.lat = req['lat']
    user.lng = req['lng']
    db.session.commit()
    return  user.to_dict()
