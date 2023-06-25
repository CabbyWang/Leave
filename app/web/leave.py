from flask import render_template, redirect, current_app, g
from flask import request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import get_debug_queries
from app.models import db

from . import web
from app.forms.auth import RegistrationForm, LoginForm
from app.models.auth import User
from app.forms.leave import ApplyForm, CancelApplyForm, ReportBackForm
from app.models.leave import Apply, Vehicle
from flask_login import current_user
from app.services.leave import ApplyService

__author__ = 'cabbyw'

from ..forms.auth import RegistrationForm
from ..view_models.apply import ApproveInfo, UserApplyInfo


@web.route('/apply', methods=['GET', 'POST'])
@login_required
def apply():
    form = ApplyForm(request.form)
    if request.method == 'POST' and form.validate():
        # 存入数据库
        ApplyService.save_apply(form)
        return redirect(url_for('web.apply_list'))
    return render_template('new_apply.html', form=form, vehicles=Vehicle.get_all_vehicles())


@web.route('/cancel', methods=['POST'])
@login_required
def cancel():
    """
    撤销申请
    :return:
    """
    form = CancelApplyForm(request.form)
    if form.validate():
        # 存入数据库
        ApplyService.cancel_apply(form)
        return redirect(url_for('web.apply_list'))
    return render_template('new_apply_list.html', form=form, vehicles=Vehicle.get_all_vehicles())


@web.route('/apply_list')
@login_required
def apply_list():
    current_user_applies = [UserApplyInfo(user_apply) for user_apply in current_user.applies]
    return render_template('new_apply_list.html', applies=current_user_applies)


@web.route('/apply_detail/<int:apply_id>')
@login_required
def apply_detail(apply_id):
    apply = Apply.query.filter_by(id=apply_id).first()
    # 通过apply_id查找到所有的审批人及审批情况
    approves = [ApproveInfo(approve) for approve in apply.approves]
    return render_template('apply_detail.html', approves=approves)


@web.route('/report_back', methods=['GET', 'POST'])
@login_required
def report_back():
    """
    销假
    :return:
    """
    if request.method == 'GET':
        return render_template('report_back.html', applies=current_user.need_report_back_applies)
    form = ReportBackForm(request.form)
    if request.method == 'POST' and form.validate():
        apply_id = form.apply_id.data
        apply = Apply.query.filter_by(id=apply_id).first()
        apply.report_back()
        return redirect(url_for('web.report_back'))
