from flask_wtf import FlaskForm

from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # id_card_number = StringField('ID Card Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')
    # submit = SubmitField('Log In')

    def validate_username(self, field):
        if 1 == 2:
            raise ValidationError('xxx')
        pass


class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    id_card_number = StringField('ID Card Number')
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # submit = SubmitField('Sign Up')
