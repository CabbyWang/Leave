from flask import render_template, redirect, current_app, g
from flask import request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import get_debug_queries
from app.models import db

from app.web import web
from app.forms.auth import RegistrationForm, LoginForm
from app.models.auth import User
from app.forms.leave import ApplyForm
from app.models.leave import Apply, Vehicle
from flask_login import current_user
from app.services.leave import ApplyService
from app.forms.admin import AddVehicleForm, DeleteVehicleForm

__author__ = 'cabbyw'


@web.route('/vehicle/del/<int:vehicle_id>', methods=['GET', 'POST'])
@login_required
def vehicle_del(vehicle_id):
    """
    删除交通工具
    :param vehicle_id:
    :return:
    """
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle:
        # TODO 这里的删除是直接删除，是否需要改变status的方式来删除？
        db.session.delete(vehicle)
        db.session.commit()
        # 删除成功
        return redirect(url_for('web.vehicle'))
    return render_template('admin/vehicle.html', vehicles=Vehicle.get_all_vehicles())


@web.route('/vehicle', methods=['GET', 'POST'])
@login_required
def vehicle():
    form = AddVehicleForm(request.form)
    if request.method == 'POST' and form.validate():
        # 添加数据
        v = Vehicle()
        v.set_attrs(form.data)
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('web.vehicle'))
    return render_template('admin/vehicle.html', vehicles=Vehicle.get_all_vehicles())



