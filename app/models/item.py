from .db import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer)
    image_src = db.Column(db.String)

    cart = db.relationship("Cart", back_populates="items")
    restaurant = db.relationship("Restaurant", back_populates="items")

    def to_dict(self):
        return {
            "id": self.id,
            "restaurant_id": self.restaurant_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "image_src": self.image_src,
        }
