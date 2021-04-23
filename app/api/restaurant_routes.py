from flask import Blueprint, jsonify, session, request
from flask_login import login_required
from app.models import db, Item, Cart, Restaurant
from app.forms import ItemForm

restaurant_routes = Blueprint('restaurants', __name__)


@restaurant_routes.route('/')
def restaurants():
    restaurants = Restaurant.query.all()
    return {"restaurants": [restaurant.to_dict() for restaurant in restaurants]}

@restaurant_routes.route('/<int:id>/')
def individualRestaurant(id):
    restaurant = Restaurant.query.get(id)
    return {"currentRestaurant" : restaurant.to_dict()}

@restaurant_routes.route('/featured/')
def featured_restaurants():
    featured = Restaurant.query.order_by(Restaurant.zip_code.asc()).limit(6).all()
    return {"restaurants": [restaurant.to_dict() for restaurant in featured]}


@restaurant_routes.route('/add-item/', methods=["POST"])
@login_required
def add_item():
    form = ItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        new_cart = Cart(user_id=form.user_id.data,
                          item_id=form.item_id.data,
                          quantity=form.quantity.data,
                          preferences=form.preferences.data)
        db.session.add(new_cart)
        db.session.commit()
        return new_cart.to_dict()
    else:
        return {"errors": "invalid submission"}

@restaurant_routes.route('/edit-item/<int:id>/', methods=["POST"])
@login_required
def edit_item(id):
    req = request.get_json()
    print('req!!', req)
    cart = Cart.query.get(id)
    cart.id = req['id']
    cart.user_id = req['user_id']
    cart.quantity = req['quantity']
    cart.preferences = req['preferences']
    db.session.commit()
    return  cart.to_dict()
