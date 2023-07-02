from flask import render_template, redirect
from flask import request, url_for
from flask_login import login_required

from app.forms.admin import AddVehicleForm
from app.models import db
from app.models.leave import Vehicle
from app.view_models.apply import VehicleInfo

from app.web import web



__author__ = 'cabbyw'


@web.route('/vehicle/del/<int:vehicle_id>', methods=['GET', 'POST'])
@login_required
def vehicle_del(vehicle_id):
    """
    删除片区
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
    return render_template('admin/vehicle.html', vehicles=[VehicleInfo(a) for a in Vehicle.get_all_vehicles()])


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
    return render_template('admin/vehicle.html', vehicles=[VehicleInfo(a) for a in Vehicle.get_all_vehicles()])



