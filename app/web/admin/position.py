from flask import render_template, redirect
from flask import request, url_for
from flask_login import login_required

from app.models import db
from app.view_models.role import PositionInfo

from app.web import web

from app.models.role import Position
from app.forms.admin import AddPositionForm


__author__ = 'cabbyw'


@web.route('/position/del/<int:position_id>', methods=['GET', 'POST'])
@login_required
def position_del(position_id):
    """
    删除岗位类别
    :param position_id:
    :return:
    """
    position = Position.query.get(position_id)
    if position:
        # TODO 这里的删除是直接删除，是否需要改变status的方式来删除？
        db.session.delete(position)
        db.session.commit()
        # 删除成功
        return redirect(url_for('web.position'))
    return render_template(
        'admin/position.html',
        positions=[PositionInfo(o) for o in Position.get_all_positions()]
    )


@web.route('/position', methods=['GET', 'POST'])
@login_required
def position():
    form = AddPositionForm(request.form)
    if request.method == 'POST' and form.validate():
        # 添加数据
        v = Position()
        v.set_attrs(form.data)
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('web.position'))
    return render_template(
        'admin/position.html',
        positions=[PositionInfo(o) for o in Position.get_all_positions()]
    )



