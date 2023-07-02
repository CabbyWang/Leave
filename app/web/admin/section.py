from flask import render_template, redirect, current_app
from flask import request, url_for
from flask_login import login_required

from app.models import db
from app.view_models.role import SectionInfo, AreaInfo, XueBuInfo

from app.web import web

from app.models.role import Section, Area, XueBu
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
    page = request.args.get('page', 1, type=int)
    pagination = Section.query.filter_by().order_by(Section.id).paginate(
        page=page, per_page=current_app.config['PAGINATION_PER_PAGE']
    )
    return render_template(
        'admin/section.html', pagination=pagination, sections=[SectionInfo(s) for s in pagination.items],
        areas=[AreaInfo(a) for a in Area.get_all_areas()],
        xuebus=[XueBuInfo(x) for x in XueBu.get_all_xuebus()],
        office_sections=[SectionInfo(s) for s in Section.query.filter_by(is_office=1).all()]
    )
    # return render_template(
    #     'admin/section.html',
    #     sections=[SectionInfo(s) for s in Section.get_all_sections()],
    #     areas=[AreaInfo(a) for a in Area.get_all_areas()],
    #     xuebus=[XueBuInfo(x) for x in XueBu.get_all_xuebus()],
    #     office_sections=[SectionInfo(s) for s in Section.query.filter_by(is_office=1).all()]
    # )



