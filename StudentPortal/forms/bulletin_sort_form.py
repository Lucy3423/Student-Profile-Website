from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class Bulletin_sort_form(FlaskForm):
    sort_types = [("all", "All"), ("upper 4", "Upper 4"), ("lower 5", "Lower 5"), ("upper 5", "Upper 5"), ("lower 6", "Lower 6"), ("upper 6", "Upper 6")] # python variable, title/label
    sort_type = RadioField("Sort Types", choices=sort_types, default="all")
    submit = SubmitField("Apply Filter")
