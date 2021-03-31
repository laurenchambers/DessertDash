from flask import Blueprint, jsonify
# from flask_login import login_required
from app.models import Restaurant

restaurant_routes = Blueprint('restaurants', __name__)


@restaurant_routes.route('/')
def restaurants():
    restaurants = Restaurant.query.all()
    return {"restaurants": [restaurant.to_dict() for restaurant in restaurants]}
