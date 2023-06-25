from datetime import datetime

from flask_login import current_user
from wtforms import form

from app.models.leave import Apply, Approve, ApproveDetail, Approving
from app.models.auth import User
from app import db


class ApproveService:
    """
    Apply服务层
    """

    @staticmethod
    def approve(approve_form):
        """
        审批流程
        1.
        2.找到规则 存入approve approve_detail approving表
        """
        approving = Approving.query.filter_by(id=approve_form.approving_id.data).first()
        approve_detail = approving.approve_detail
        approve = approve_detail.approve
        if approve_form.approve_result.data == 'approve':
            # 审批通过流程
            with db.auto_commit():
                # 1. 修改approve_detail表审核状态->3
                approve_detail.approve_status = 3
                # 2. 删除approving
                # approving.delete()
                db.session.delete(approving)
                # 3. 获取下一个审批人的审批明细
                next_approve_detail = ApproveDetail.query.filter_by(approve_id=approve_detail.approve_id,
                                                                    approve_status=1).first()
                if not next_approve_detail:
                    # 4. 如果没有下一个审批人 审批通过 Approve 状态->3
                    approve.approve_status = 3
                else:
                    # 4. 如果有下一个审批人 next ApproveDetail 状态->2(待审批) & 写入Approving
                    next_approve_detail.approve_status = 2
                    next_approving = Approving()
                    next_approving.approver = next_approve_detail.approver
                    next_approving.approve_detail = next_approve_detail
                    db.session.add(next_approving)
        elif approve_form.approve_result.data == 'reject':
            # 审批驳回流程
            with db.auto_commit():
                # 1. ApproveDetail 状态->4(驳回)
                approve_detail.approve_status = 4
                # 2. 删除Approving
                # approving.delete()
                db.session.delete(approving)
                # 3. 修改Approve 状态->4(驳回)
                approve.approve_status = 4
