from .db import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)
    name = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_src = db.Column(db.Text)

    cart = db.relationship("Cart", back_populates="items")
    restaurant = db.relationship("Restaurant", back_populates="items")

    def to_dict(self):
        return {
            "id": self.id,
            "restaurant_id": self.restaurant_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_src": self.image_src,
        }


    # def to_simple_dict(self):
    #     items = []

    #     for cart in self.cart:
    #         items.append(cart.get_item())

    #     if len(items) == 1:
    #         totalItems = items[0]
    #     else:
    #         totalItems = items

    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "price": self.price,
    #         "items": totalItems
    #     }
