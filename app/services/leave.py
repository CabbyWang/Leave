from datetime import datetime

from flask_login import current_user
from wtforms import form

from app.models.leave import Apply, Approve, ApproveDetail, Approving
from app.models.auth import User
from app import db


class ApplyService:
    """
    Apply服务层
    """

    @staticmethod
    def save_apply(apply_form):
        """
        1.存储至Apply表
        2.找到规则 存入approve approve_detail approving表
        :param apply_form:
        :return:
        """
        with db.auto_commit():
            apply = Apply()
            apply.applicant = current_user
            apply.vehicle_id = apply_form.data['vehicle_id']
            apply.destination = apply_form.data['destination']
            apply.cause = apply_form.data['cause']
            apply.leave_date = apply_form.data['leave_date']
            apply.back_date = apply_form.data['back_date']
            db.session.add(apply)
            # 添加到审批表approve
            approve = Approve()
            approve.apply = apply
            approve.applicant = current_user
            db.session.add(approve)
            # 通过当前用户获取所有需要授权的人
            approvers = current_user.get_all_approver()
            for index, approver in enumerate(approvers):
                detail = ApproveDetail()
                detail.approve = approve
                detail.approver = approver
                # 默认将第一个人设置为待我审批
                if index == 0:
                    detail.approve_status = 2  # 待我审批
                    # 写入approving表
                    approving = Approving()
                    approving.approve_detail = detail
                    approving.approver = approver
                    db.session.add(approving)
                db.session.add(detail)

    @staticmethod
    def cancel_apply(cancel_apply_form):
        """
        1.Approve 状态-> 2 (撤销)
        2.ApproveDetail 状态-> 1 (审核中)
        3.Approving 删除
        :return:
        """
        with db.auto_commit():
            apply_id = cancel_apply_form.apply_id.data
            apply = Apply.query.filter_by(id=apply_id).first()
            approve = apply.approve
            approve.approve_status = 2
            for approve_detail in approve.approve_details:
                approve_detail.approve_status = 1
                approving = approve_detail.approving
                if approving:
                    db.session.delete(approving)

    @staticmethod
    def report_back(report_back_form):
        """
        1.Approve 状态-> 2 (撤销)
        2.ApproveDetail 状态-> 1 (审核中)
        3.Approving 删除
        :return:
        """
        with db.auto_commit():
            apply_id = report_back_form.apply_id.data


# class LeaveService:
#     @staticmethod
#     def get_all_leaves():
#         leaves = Leave.query.all()
#         return [leave.to_dict() for leave in leaves]
#
#     @staticmethod
#     def get_leave(id):
#         leave = Leave.query.get(id)
#         if leave is None:
#             return None
#         return leave.to_dict()
#
#     @staticmethod
#     def create_leave(user_id, start_time, end_time, reason):
#         leave = Leave(
#             user_id=user_id,
#             start_time=datetime.fromisoformat(start_time),
#             end_time=datetime.fromisoformat(end_time),
#             reason=reason,
#             status=0
#         )
#         db.session.add(leave)
#         db.session.commit()
#         return leave.to_dict()
#
#     @staticmethod
#     def update_leave(id, user_id, start_time, end_time, reason, status):
#         leave = Leave.query.get(id)
#         if leave is None:
#             return None
#         leave.user_id = user_id
#         leave.start_time = datetime.fromisoformat(start_time)
#         leave.end_time = datetime.fromisoformat(end_time)
#         leave.reason = reason
#         leave.status = status
#         db.session.commit()
#         return leave.to_dict()
#
#     @staticmethod
#     def delete_leave(id):
#         leave = Leave.query.get(id)
#         if leave is None:
#             return False
#         db.session.delete(leave)
#         db.session.commit()
#         return True