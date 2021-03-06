from .db import db
from app.models import restaurants_genres

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    img_src = db.Column(db.String, nullable=False)

    restaurants = db.relationship("Restaurant", secondary=restaurants_genres, back_populates="genres")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "img_src": self.img_src
        }

    def to_all_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "restaurants": [restaurant.to_simple_dict() for restaurant in self.restaurants],
        }
