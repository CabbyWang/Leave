from flask_wtf import FlaskForm

from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, Field
from wtforms.validators import DataRequired, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # id_card_number = StringField('ID Card Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    # submit = SubmitField('Log In')

    # def validate_username(self, field):
    #     if 1 == 2:
    #         raise ValidationError('xxx')
    #     pass


class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    id_card_number = StringField('ID Card Number')
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    section_id = IntegerField('Section')
    occupation_id = IntegerField('Occupation')
    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # submit = SubmitField('Sign Up')


class IntegerNullField(IntegerField):
    def _value(self):
        if self.raw_data:
            return self.raw_data[0]
        if self.data is not None:
            return str(self.data)
        return ""


class UserForm(Form):
    name = StringField('name')
    username = StringField('Username', validators=[DataRequired()])
    id_card_number = StringField('ID Card Number')
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    # section_id = IntegerField(default=0)
    # occupation_id = IntegerField(default=0)
    section_id = Field()  # TODO 完全没限制,是否有风险?
    is_committee_member = Field()
    xuebu_id = Field()
    area_id = Field()
    occupation_id = Field()
    position_id = Field()
    level_id = Field()

    # def validate_occupation_id(self, field):
    #     if not field:
    #         self.occupation_id = None
    #
    # def validate_section_id(self, field):
    #     if not field:
    #         self.occupation_id = None

    # def validate_level_id(self, field):
    #     pass
