from flask import render_template, redirect
from flask_login import login_required

from app.web import web
from app.models.role import Level


__author__ = 'cabbyw'


@web.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return render_template('admin/admin.html')


@web.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    return render_template('admin/level.html')


