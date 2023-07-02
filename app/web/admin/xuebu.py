from flask import render_template, redirect
from flask import request, url_for
from flask_login import login_required

from app.models import db
from app.view_models.role import XueBuInfo

from app.web import web

from app.models.role import XueBu
from app.forms.admin import AddXuebuForm


__author__ = 'cabbyw'


@web.route('/xuebu/del/<int:xuebu_id>', methods=['GET', 'POST'])
@login_required
def xuebu_del(xuebu_id):
    """
    删除部门
    :param section_id:
    :return:
    """
    xuebu = XueBu.query.get(xuebu_id)
    if xuebu:
        # TODO 这里的删除是直接删除，是否需要改变status的方式来删除？
        db.session.delete(xuebu)
        db.session.commit()
        # 删除成功
        return redirect(url_for('web.xuebu'))
    return render_template('admin/xuebu.html', xuebus=[XueBuInfo(x) for x in XueBu.get_all_xuebus()])


@web.route('/xuebu', methods=['GET', 'POST'])
@login_required
def xuebu():
    form = AddXuebuForm(request.form)
    if request.method == 'POST' and form.validate():
        # 添加数据
        v = XueBu()
        v.set_attrs(form.data)
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('web.xuebu'))
    return render_template('admin/xuebu.html', xuebus=[XueBuInfo(x) for x in XueBu.get_all_xuebus()])



