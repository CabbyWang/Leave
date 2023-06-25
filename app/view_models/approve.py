from datetime import datetime
from app.models.auth import User


class UserApproveDetail:

    def __init__(self, approve):
        apply = approve.apply
        self.id = approve.id
        self.apply_time = datetime.fromtimestamp(apply.create_time)
        self.vehicle = apply.vehicle.name
        self.destination = apply.destination
        self.leave_date = apply.leave_date
        self.back_date = apply.back_date


class ApproveInfo:

    def __init__(self, approve):
        self.approve_time = datetime.now()
        self.approver = User.query.filter_by(id=approve.approve_user_id).first().name
        self.approved = approve.approved and '审批通过' or '未审批'
        self.active = 'active' if approve.approved else ''


class ApprovingInfo:

    def __init__(self, approving):
        # 申请人
        self.approving_id = approving.id
        self.approve = approving.approve_detail.approve
        # self.approve_detail_id =
        apply = self.approve.apply
        self.applicant_section = apply.applicant.section.name
        self.applicant_name = self.approve.applicant.name  # 申请人
        # self.applicant_section_name =
        self.apply_time = datetime.fromtimestamp(apply.create_time)  # 申请时间
        self.vehicle = apply.vehicle.name  # 交通工具
        self.destination = apply.destination  # 目的地
        self.leave_date = apply.leave_date  # 离开时间
        self.back_date = apply.back_date  # 返回时间

    @property
    def approve_status(self):
        # 1.待审 2.通过 3.驳回 4.撤销
        status_map = {1: '待审', 2: '撤销', 3: '通过', 4: '驳回'}
        return status_map[self.approve.approve_status]


class ApprovedInfo:

    def __init__(self, approve_detail):
        # 申请人
        self.approve = approve_detail.approve
        # self.approve_detail_id =
        apply = self.approve.apply
        self.applicant_section = apply.applicant.section.name
        self.applicant_name = self.approve.applicant.name  # 申请人
        # self.applicant_section_name =
        self.apply_time = datetime.fromtimestamp(apply.create_time)  # 申请时间
        self.vehicle = apply.vehicle.name  # 交通工具
        self.destination = apply.destination  # 目的地
        self.leave_date = apply.leave_date  # 离开时间
        self.back_date = apply.back_date  # 返回时间

    @property
    def approve_status(self):
        # 1.待审 2.通过 3.驳回 4.撤销
        status_map = {1: '待审', 2: '撤销', 3: '通过', 4: '驳回'}
        return status_map[self.approve.approve_status]


class CurrentUserApprovingInfo:
    """
    当天用户的待审信息
    : 部门 + 申请人姓名 + '的请假申请'
    : create_time
    """

    def __init__(self, approving):
        approve = approving.approve_detail.approve
        applicant = approve.applicant
        self.applicant_name = applicant.name
        self.section = applicant.section.name
        self.create_time = approve.create_datetime
