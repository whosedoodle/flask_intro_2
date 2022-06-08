from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    address = PasswordField('Address', validators=[DataRequired()])
    submit = SubmitField()