from .db import db

class Cart(db.Model):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)
    quantity = db.Column(db.Integer)
    preferences = db.Column(db.Text)

    user = db.relationship("User", back_populates="cart")
    items = db.relationship("Item", back_populates="cart")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "quantity": self.quantity,
            "preferences": self.preferences,
            "item_name": self.items.name,
            "item_price": self.items.price,
            "item_description": self.items.description,
            "item_image_src": self.items.image_src,
            "item_id": self.items.id
        }

    def to_full_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "quantity": self.quantity,
            "preferences": self.preferences,
            "item_name": self.items.name,
            "item_price": self.items.price,
            "item_description": self.items.description,
            "item_image_src": self.items.image_src,
        }


