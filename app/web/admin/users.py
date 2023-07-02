from flask import render_template, redirect, current_app
from flask import request, url_for
from flask_login import login_required

from app.models import db
from app.view_models.role import PositionInfo, LevelInfo, AreaInfo, XueBuInfo, SectionInfo, OccupationInfo
from app.view_models.users import UserInfo
from app.forms.auth import RegistrationForm, UserForm

from app.web import web

from app.models.auth import User
from app.models.role import Section, Level, Occupation, XueBu, Area, Position


__author__ = 'cabbyw'


@web.route('/user/del/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_del(user_id):
    """
    删除用户
    :param user_id:
    :return:
    """
    user = User.query.get(user_id)
    if user:
        # TODO 这里的删除是直接删除，是否需要改变status的方式来删除？
        db.session.delete(user)
        db.session.commit()
        # 删除成功
        return redirect(url_for('web.user'))
    return render_template(
        'admin/user.html', users=[UserInfo(u) for u in User.get_all_users()]
    )


@web.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.filter_by().order_by(User.id).paginate(
        page=page, per_page=current_app.config['PAGINATION_PER_PAGE']
    )
    return render_template(
        'admin/users.html', pagination=pagination, users=[UserInfo(u) for u in pagination.items]
    )


@web.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user(user_id):
    # TODO 404 用户信息不存在处理?
    u = User.query.filter_by(id=user_id).first()
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        # 修改
        u.set_attrs(form.data)
        db.session.commit()
        return redirect(url_for('web.user', user_id=user_id))
    return render_template(
        'admin/user.html', user_id=u.id, user=UserInfo(u),
        sections=[SectionInfo(s) for s in Section.get_all_sections()],
        xuebus=[XueBuInfo(x) for x in XueBu.get_all_xuebus()],
        areas=[AreaInfo(a) for a in Area.get_all_areas()],
        occupations=[OccupationInfo(o) for o in Occupation.get_all_occupations()],
        levels=[LevelInfo(level) for level in Level.get_all_levels()],
        positions=[PositionInfo(p) for p in Position.get_all_positions()],
        form=form
    )


