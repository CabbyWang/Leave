from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, IntegerField


class DeleteVehicleForm(FlaskForm):

    # name = StringField('name')
    id = IntegerField('id')
    delete = SubmitField('删除')


class AddVehicleForm(FlaskForm):

    name = StringField('vehicle')
    add = SubmitField('新增')


class AddVehicleForm(Form):

    name = StringField('vehicle')


class AddLevelForm(Form):
    name = StringField('vehicle')


class AddOccupationForm(Form):

    name = StringField('occupation')


class AddSectionForm(Form):

    name = StringField('section')


class AddRuleForm(Form):

    section_id = IntegerField('section_id')
    occupation_id = IntegerField('occupation_id')
    level_id = IntegerField('level_id')
