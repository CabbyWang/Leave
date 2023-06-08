from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ApplyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # id_card_number = StringField('ID Card Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # remember_me = BooleanField('Remember Me')
    # submit = SubmitField('Log In')

    def validate_username(self, field):
        if 1 == 2:
            raise ValidationError('xxx')
        pass
