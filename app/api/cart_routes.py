from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Cart, db

cart_routes = Blueprint('carts', __name__)


@cart_routes.route('/')
def carts():
    carts = Cart.query.all()
    return {"cart": [cart.to_dict() for cart in carts]}

@cart_routes.route("/<int:id>/delete/", methods=["GET"])
def remove_cart(id):
    cart = Cart.query.get(id)
    db.session.delete(cart)
    db.session.commit()
    return {"deleted": id}
