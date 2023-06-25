from flask import render_template, redirect
from flask import request, url_for
from flask_login import login_required

from app.models import db
from app.view_models.users import UserInfo
from app.forms.auth import RegistrationForm, UserForm

from app.web import web

from app.models.auth import User
from app.models.role import Section, Level, Occupation
# from app.forms.admin import AddUserForm


__author__ = 'cabbyw'


@web.route('/user/del/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_del(user_id):
    """
    删除审批规则
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
    return render_template('admin/user.html', users=user.get_all_users())


@web.route('/users', methods=['GET', 'POST'])
@login_required
def users():

    return render_template('admin/users.html', users=User.get_all_users())


@web.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user(user_id):
    # TODO 404 用户信息不存在处理?
    u = User.query.filter_by(id=user_id).first()
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        # 修改
        u.set_attrs(form.data)

        # db.session.add(u)
        db.session.commit()
        return redirect(url_for('web.user', user_id=user_id))
    return render_template(
        'admin/user.html', user=UserInfo(u),
        sections=Section.get_all_sections(),
        occupations=Occupation.get_all_occupations(),
        leavls=Level.get_all_levels(),
        form=form
    )


