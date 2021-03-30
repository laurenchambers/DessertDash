from .db import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


restaurants_genres = db.Table(
    "restaurants_genres",
    db.Column("restaurant_id", db.Integer, db.ForeignKey("restaurants.id"), primary_key=True),
    db.Column("genre_id", db.Integer, db.ForeignKey("genres.id"), primary_key=True))
