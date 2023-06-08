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




