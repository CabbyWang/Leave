from wtforms import Form, StringField, SelectMultipleField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime


class DropdownVehicle(Form):

    vehicle = SelectMultipleField('交通工具', choices=[(1, '火车'), (2, '汽车')])


class ApplyForm(Form):
    vehicle_id = IntegerField('Vehicle', validators=[DataRequired()])
    # vehicle = Column(String, nullable=False, comment='交通工具')
    destination = StringField('Destination', validators=[DataRequired()])
    cause = StringField('cause', validators=[DataRequired()])
    leave_date = DateField('Leave_date', validators=[DataRequired()])
    back_date = DateField('Back_date', validators=[DataRequired()])


class CancelApplyForm(Form):
    apply_id = IntegerField('Apply id', validators=[DataRequired()])


class ReportBackForm(Form):
    apply_id = IntegerField('Apply id', validators=[DataRequired()])
