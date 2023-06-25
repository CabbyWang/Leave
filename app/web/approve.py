from flask import render_template, redirect, current_app, g
from flask import request, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc

from . import web
from app.forms.approve import ApproveForm
from app.models.leave import Approve, Vehicle, ApproveDetail, Approving
from flask_login import current_user
# from app.services.leave import ApproveService

__author__ = 'cabbyw'

from .. import db
from ..forms.auth import RegistrationForm
from app.view_models.approve import ApproveInfo, UserApproveDetail, ApprovingInfo, ApprovedInfo
from app.view_models.apply import UserApplyInfo
from ..services.approve import ApproveService


# @web.route('/approve', methods=['GET', 'POST'])
# @login_required
# def approve():
#     form = ApproveForm(request.form)
#     if request.method == 'POST' and form.validate():
#         # 存入数据库
#         # ApproveService.save_approve(form)
#         return redirect(url_for('web.approve'))
#     return render_template('approve.html', form=form, vehicles=Vehicle.get_all_vehicles())


@web.route('/approving_list', methods=['GET', 'POST'])
@login_required
def approving_list():
    """
    待审批列表
    :return: 当前审批用户待审，从审批明细表中获取
    """
    approving_details = Approving.query.filter_by(approver=current_user).all()
    approving_list = [ApprovingInfo(approving_detail) for approving_detail in approving_details]
    return render_template('new_approving_list.html', approving_list=approving_list)


@web.route('/approved_list')
@login_required
def approved_list():
    """
    已审批列表
    :return:
    """
    approved_details = ApproveDetail.query.filter_by(approver=current_user).filter(
        ApproveDetail.approve_status.in_((3, 4))
        ).all()
    approved_list = [ApprovedInfo(approved_detail) for approved_detail in approved_details]
    return render_template('new_approved_list.html', approved_list=approved_list)


@web.route('/approve_list')
@login_required
def approve_list():
    # 当前用户所有的审批记录 Approve
    pass
    # user_id = current_user.id
    # applies = [UserApplyDetail(approve.apply) for approve in Approve.query.filter_by(
    #     approve_user_id=user_id, approved=False
    # ).order_by(desc(Approve.create_time)).all()]
    # return render_template('approve/approve_list.html', applies=applies)


@web.route('/approve_detail/<int:approve_id>')
@login_required
def approve_detail(approve_id):
    approve = Approve.query.filter_by(id=approve_id).first()
    # 通过approve_id查找到所有的审批人及审批情况
    approves = [ApproveInfo(approve) for approve in approve.approves]
    return render_template('approve/approve_detail.html', approves=approves)


@web.route('/approve', methods=['POST'])
@login_required
def approve():
    """
    审核
    :return:
    """
    form = ApproveForm(request.form)
    approving_details = Approving.query.filter_by(approver=current_user).all()
    approving_list = [ApprovingInfo(approving_detail) for approving_detail in approving_details]
    if not form.validate():
        return render_template('new_approving_list.html', approving_list=approving_list)
    ApproveService.approve(form)
    # return redirect(url_for('web.approving_list', approving_list=approving_list))
    return redirect(url_for('web.approving_list'))
