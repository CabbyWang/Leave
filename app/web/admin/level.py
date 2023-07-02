from flask import render_template, redirect, current_app, g
from flask import request, flash, url_for
from flask_login import login_required

from app.models import db
from app.view_models.role import LevelInfo

from app.web import web

from app.models.leave import Apply, Vehicle
from app.models.role import Level
from app.forms.admin import AddLevelForm


__author__ = 'cabbyw'


@web.route('/level/del/<int:level_id>', methods=['GET', 'POST'])
@login_required
def level_del(level_id):
    """
    删除审批级别
    :param level_id:
    :return:
    """
    level = Level.query.get(level_id)
    if level:
        # TODO 这里的删除是直接删除，是否需要改变status的方式来删除？
        db.session.delete(level)
        db.session.commit()
        # 删除成功
        return redirect(url_for('web.level'))
    return render_template(
        'admin/level.html', levels=[LevelInfo(lev) for lev in Level.get_all_levels()]
    )


@web.route('/level', methods=['GET', 'POST'])
@login_required
def level():
    form = AddLevelForm(request.form)
    if request.method == 'POST' and form.validate():
        # 添加数据
        v = Level()
        v.set_attrs(form.data)
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('web.level'))
    return render_template(
        'admin/level.html', levels=[LevelInfo(lev) for lev in Level.get_all_levels()]
    )
