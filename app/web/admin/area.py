from flask import render_template, redirect
from flask import request, url_for
from flask_login import login_required

from app.models import db
from app.view_models.role import AreaInfo

from app.web import web

from app.models.role import Area
from app.forms.admin import AddAreaForm


__author__ = 'cabbyw'


@web.route('/area/del/<int:area_id>', methods=['GET', 'POST'])
@login_required
def area_del(area_id):
    """
    删除片区
    :param area_id:
    :return:
    """
    area = Area.query.get(area_id)
    if area:
        # TODO 这里的删除是直接删除，是否需要改变status的方式来删除？
        db.session.delete(area)
        db.session.commit()
        # 删除成功
        return redirect(url_for('web.area'))
    return render_template('admin/area.html', areas=[AreaInfo(a) for a in Area.get_all_areas()])


@web.route('/area', methods=['GET', 'POST'])
@login_required
def area():
    form = AddAreaForm(request.form)
    if request.method == 'POST' and form.validate():
        # 添加数据
        v = Area()
        v.set_attrs(form.data)
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('web.area'))
    return render_template('admin/area.html', areas=[AreaInfo(a) for a in Area.get_all_areas()])



