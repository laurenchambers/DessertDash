from .db import db
from app.models import restaurants_genres

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    hours = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    logo_src = db.Column(db.String)

    genres = db.relationship("Genre", secondary=restaurants_genres, back_populates="restaurants")
    items = db.relationship("Item", back_populates="restaurant")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "lat": self.lat,
            "lng": self.lng,
            "hours": self.hours,
            "price": self.price,
            "rating": self.rating,
            "logo_src": self.logo_src,
            "genres": [genre.to_dict() for genre in self.genres],
            "items": [item.to_dict() for item in self.items],
        }

    def to_simple_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "address": self.address,
                "city": self.city,
                "state": self.state,
                "zip_code": self.zip_code,
                "lat": self.lat,
                "lng": self.lng,
                "hours": self.hours,
                "price": self.price,
                "rating": self.rating,
                "logo_src": self.logo_src,
                "items": [item.to_dict() for item in self.items],
        }
