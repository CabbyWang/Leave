from datetime import datetime
from app.models.auth import User


class UserApplyInfo:

    def __init__(self, apply):
        self.apply = apply
        self.id = apply.id
        self.create_time = datetime.fromtimestamp(apply.create_time)
        self.section_name = apply.applicant.section.name
        self.apply_name = apply.applicant.name
        self.apply_section = apply.applicant.section.name
        self.destination = apply.destination
        self.vehicle = apply.vehicle.name
        self.leave_date = apply.leave_date
        self.back_date = apply.back_date

    @property
    def actual_back_date(self):
        actual_back_date = self.apply.actual_back_date
        return actual_back_date and actual_back_date.strftime('%Y-%m-%d %H:%M') or ''

    @property
    def approve_status(self):
        approve = self.apply.approve
        # 1.待审 2.通过 3.驳回 4.撤销
        status_map = {1: '待审', 2: '撤销', 3: '通过', 4: '驳回'}
        return status_map[approve.approve_status]


class ApproveInfo:

    def __init__(self, approve):
        self.approve_time = datetime.now()
        self.approver = User.query.filter_by(id=approve.approve_user_id).first().name
        self.approved = approve.approved and '审批通过' or '未审批'
        self.active = 'active' if approve.approved else ''
