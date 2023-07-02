from flask import render_template, redirect
from flask import request, url_for
from flask_login import login_required

from app.models import db
from app.view_models.role import OccupationInfo

from app.web import web

from app.models.role import Occupation
from app.forms.admin import AddOccupationForm


__author__ = 'cabbyw'


@web.route('/occupation/del/<int:occupation_id>', methods=['GET', 'POST'])
@login_required
def occupation_del(occupation_id):
    """
    删除人员类别
    :param occupation_id:
    :return:
    """
    occupation = Occupation.query.get(occupation_id)
    if occupation:
        # TODO 这里的删除是直接删除，是否需要改变status的方式来删除？
        db.session.delete(occupation)
        db.session.commit()
        # 删除成功
        return redirect(url_for('web.occupation'))
    return render_template(
        'admin/occupation.html',
        occupations=[OccupationInfo(o) for o in Occupation.get_all_occupations()]
    )


@web.route('/occupation', methods=['GET', 'POST'])
@login_required
def occupation():
    form = AddOccupationForm(request.form)
    if request.method == 'POST' and form.validate():
        # 添加数据
        v = Occupation()
        v.set_attrs(form.data)
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('web.occupation'))
    return render_template(
        'admin/occupation.html',
        occupations=[OccupationInfo(o) for o in Occupation.get_all_occupations()]
    )



