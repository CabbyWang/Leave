from flask import render_template, redirect, current_app, g
from flask import request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import get_debug_queries
from app.models import db

from . import web
from app.forms.auth import RegistrationForm, LoginForm
from app.models.auth import User
from app.models import base

__author__ = 'cabbyw'

from ..forms.auth import RegistrationForm
from wtforms import Form


@web.route('/')
@login_required
def index():
    form = Form()
    return render_template('admin.html', form=Form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    a = form.validate_on_submit()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash("账号或密码错误", category='login_error')
    return render_template('login.html', form=form)


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(
        #     username=form.username.data,
        #     id_card_number=form.id_card_number.data,
        #     password=form.password.data,
        #     phone_number=form.phone_number.data
        # )
        user = User()
        user.set_attrs(form.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('register.html', form=form)




