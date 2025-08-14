from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class Bulletin_sort_form(FlaskForm):
    sort_types = [('recent', "Most Recent"), ("oldest", "Oldest")] # python variable, title/label
    sort_type = RadioField("Sort Types", choices=sort_types)
    submit = SubmitField("Apply Filter")
