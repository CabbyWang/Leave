from flask import render_template, redirect
from flask import request, url_for
from flask_login import login_required

from app.models import db

from app.web import web

from app.models.role import Section
from app.forms.admin import AddSectionForm


__author__ = 'cabbyw'


@web.route('/section/del/<int:section_id>', methods=['GET', 'POST'])
@login_required
def section_del(section_id):
    """
    删除部门
    :param section_id:
    :return:
    """
    section = Section.query.get(section_id)
    if section:
        # TODO 这里的删除是直接删除，是否需要改变status的方式来删除？
        db.session.delete(section)
        db.session.commit()
        # 删除成功
        return redirect(url_for('web.section'))
    return render_template('admin/section.html', sections=Section.get_all_sections())


@web.route('/section', methods=['GET', 'POST'])
@login_required
def section():
    form = AddSectionForm(request.form)
    if request.method == 'POST' and form.validate():
        # 添加数据
        v = Section()
        v.set_attrs(form.data)
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('web.section'))
    return render_template('admin/section.html', sections=Section.get_all_sections())



