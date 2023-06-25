from wtforms import Form, StringField, IntegerField, DateField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime


class ApproveForm(Form):
    approving_id = IntegerField('Approving ID', validators=[DataRequired()])
    approve_result = SelectField('Approve Result', choices=[('approve', '通过'), ('reject', '驳回')])



