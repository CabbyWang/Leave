from flask import render_template, redirect, current_app, g
from flask import request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import get_debug_queries
from flask_wtf import csrf

from app.models import db

from . import web
from app.forms.auth import RegistrationForm, LoginForm
from app.models.auth import User
from app.models import base

__author__ = 'cabbyw'

from ..forms.auth import RegistrationForm
from ..models.role import Occupation, Section
from ..view_models.role import OccupationInfo, SectionInfo


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash("账号或密码错误", category='login_error')
    return render_template('new_login.html', form=form)


@web.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm(request.form)
    if User.query.filter_by(username=form.username.data).first():
        flash('用户名已存在, 请重试')
    elif request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template(
        'new_register.html', form=form,
        occupations=[OccupationInfo(o) for o in Occupation.get_all_occupations()],
        sections=[SectionInfo(s) for s in Section.get_all_sections()]
    )


@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.login'))




