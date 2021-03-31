from flask import Blueprint, jsonify
# from flask_login import login_required
from app.models import Genre

genre_routes = Blueprint('genres', __name__)


@genre_routes.route('/')
def genres():
    genres = Genre.query.all()
    return {"genres": [genre.to_dict() for genre in genres]}
