from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    user_id = IntegerField("user_id", validators=[DataRequired()])
    item_id = IntegerField("item_id", validators=[DataRequired()])
    quantity = IntegerField("quantity")
    preferences = TextField("preferences")
