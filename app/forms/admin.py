from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, IntegerField, Field
from wtforms.validators import DataRequired


class DeleteVehicleForm(FlaskForm):

    # name = StringField('name')
    id = IntegerField('id')
    delete = SubmitField('删除')


class AddVehicleForm(FlaskForm):

    name = StringField('vehicle', validators=[DataRequired()])
    add = SubmitField('新增')


class AddVehicleForm(Form):

    name = StringField('vehicle', validators=[DataRequired()])


class AddLevelForm(Form):
    name = StringField('level', validators=[DataRequired()])


class AddOccupationForm(Form):

    name = StringField('occupation', validators=[DataRequired()])


class AddSectionForm(Form):

    name = StringField('section', validators=[DataRequired()])
    area_id = Field()
    xuebu_id = Field()
    is_office = Field()
    parent_id = Field()


class AddXuebuForm(Form):

    name = StringField('section', validators=[DataRequired()])


class AddAreaForm(Form):

    name = StringField('section', validators=[DataRequired()])


class AddVehicleForm(Form):

    name = StringField('vehicle', validators=[DataRequired()])


class AddPositionForm(Form):

    name = StringField('position', validators=[DataRequired()])


class AddRuleForm(Form):

    section_id = IntegerField('section_id')
    occupation_id = IntegerField('occupation_id')
    level_id = IntegerField('level_id')
