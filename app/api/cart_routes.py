from flask import Blueprint, jsonify
# from flask_login import login_required
from app.models import Cart

cart_routes = Blueprint('carts', __name__)


@cart_routes.route('/')
def carts():
    carts = Cart.query.all()
    return {"cart": [cart.to_dict() for cart in carts]}
