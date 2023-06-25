from datetime import datetime, timedelta

from sqlalchemy.orm import relationship

from app.models.base import Base, db
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Date, Boolean


class Vehicle(Base):
    """
    交通工具表
    """

    __table_name = 'vehicle'

    id = Column(Integer, autoincrement=True, primary_key=True, comment='id')
    name = Column(String, unique=True, comment='交通工具名(火车/高铁/飞机/自驾...其他)')
    # applies = relationship('Apply', backref='vehicle', lazy='dynamic')

    # 获取所有的交通方式
    @classmethod
    def get_all_vehicles(cls):
        # {1: '火车', 2: '其他'}
        return {a.id: a.name for a in cls.query.filter_by().order_by(cls.id).all()}


class Apply(Base):
    """
    请假申请表
    """
    __tablename__ = 'apply'

    id = Column(Integer, autoincrement=True, primary_key=True, comment='apply_id')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    # user = relationship('User', backref='applies')
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False, comment='交通工具')
    vehicle = relationship('Vehicle')
    # vehicle = Column(String, nullable=False, comment='交通工具')
    destination = Column(String(100), nullable=False, comment='目的地')
    cause = Column(String(200), nullable=False, comment='请假原因')
    leave_date = Column(Date, nullable=False, comment='离开日期')
    back_date = Column(Date, nullable=False, comment='返回日期')
    actual_back_date = Column(DateTime, nullable=True, comment='实际返回时间')
    outdays = Column(Integer, default=0, comment='外出天数')
    # approved = Column(Boolean, default=False, comment='是否审批通过.有多个审批人时,全部审批完,才为True')
    approve = relationship('Approve', backref='apply', uselist=False)

    def report_back(self):
        """
        销假
        :return:
        """
        with db.auto_commit():
            now = datetime.now()
            # Apply添加实际返回日期
            self.actual_back_date = now
            # 计算外出天数 TODO 计算算法，具体如何判定外出天数？提前销假如何处理？暂定后一天12：00前销假算正常休假,否则多算一天
            if now.date() < self.back_date + timedelta(hours=36):
                outdays = (self.back_date - self.leave_date).days + 1
            else:
                # 超过12点前销假
                outdays = (now.date() - self.leave_date).days + 1
            self.outdays = outdays


# class Leave(Base):
#     """
#     请假表(暂时不需要)
#     """
#     __tablename__ = 'leave'
#
#     id = Column(Integer, primary_key=True)


class Approve(Base):
    """
    审批主表
    """
    __tablename__ = 'approve'

    id = Column(Integer, autoincrement=True, primary_key=True, comment='approve_id')
    apply_id = Column(Integer, ForeignKey('apply.id'), nullable=False, comment='申请表id')
    # apply = relationship('Apply')
    applicant_id = Column(Integer, ForeignKey('users.id'), nullable=False, comment='申请人')
    # approve_user_id = Column(Integer, nullable=False)  # 不用外键,直接存储
    approve_status = Column(Integer, default=1, comment='审批状态 1:待审 2:通过 3:驳回 4:撤销')
    # approved_time = Column(DateTime, comment='审批时间')
    approve_details = relationship('ApproveDetail', backref='approve')


class ApproveDetail(Base):
    """
    审批明细表
    : 插入审批主表时生成，决定审批流程
    """
    __tablename__ = 'approve_detail'

    id = Column(Integer, autoincrement=True, primary_key=True, comment='approve_detail_id')
    approve_id = Column(Integer, ForeignKey('approve.id'), nullable=False, comment='审核主表id')
    approver_id = Column(Integer, ForeignKey('users.id'), nullable=False, comment='审批人')  # 不用外键,直接存储
    memo = Column(String, comment='备注')
    approve_status = Column(Integer, default=1, comment='审批状态: 1:审核中 2:待我审批 3:通过 4:驳回')
    approving = relationship('Approving', backref='approve_detail', uselist=False)  # 一对一


class Approving(Base):
    """
    待审批队列
    : 将待我审批状态的审批人放入此表
    : 方便查询，用于通知审批人
    """
    __tablename__ = 'approving'

    id = Column(Integer, autoincrement=True, primary_key=True, comment='approving_id')
    approve_detail_id = Column(Integer, ForeignKey('approve_detail.id'), comment='审批明细表id')
    approver_id = Column(Integer, ForeignKey('users.id'), nullable=False, comment='审核人')
