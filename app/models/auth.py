from flask_login import UserMixin
from sqlalchemy.orm import relationship

from flask import current_app
from sqlalchemy.testing import in_

from app import login_manager
from app.models.base import Base, db
from sqlalchemy import Column, String, Integer, ForeignKey, func, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=True)
    username = Column(String(30), unique=True, nullable=False)
    _password = Column('password', String(110), nullable=False)
    phone_number = Column(String(18))
    id_card_number = Column(String(18))
    status = Column(SmallInteger, default=1)
    # section = relationship('Section', back_populates='users')
    is_committee_member = Column(Integer, default=0, comment='是否是中心其他常委')
    section_id = Column(Integer, ForeignKey('section.id'), nullable=True, comment='科室或部门')
    xuebu_id = Column(Integer, ForeignKey('xuebu.id'), nullable=True, comment='学部')
    area_id = Column(Integer, ForeignKey('area.id'), nullable=True, comment='片区')
    occupation_id = Column(Integer, ForeignKey('occupation.id'), nullable=True, comment='人员类别')
    position_id = Column(Integer, ForeignKey('position.id'), comment='岗位类别')
    # level = relationship('Level')
    level_id = Column(Integer, ForeignKey('level.id'), nullable=True, comment='审批级别')
    applies = relationship('Apply', backref='applicant', order_by='Apply.create_time.desc()')
    approves = relationship('Approve', backref='applicant')
    approve_details = relationship('ApproveDetail', backref='approver')
    approvings = relationship('Approving', backref='approver')

    @property
    def password(self):
        return self._password

    @property
    def is_active(self):
        # TODO 如果没有被分配岗位，则为False(需求：人力资源激活账号后才能使用)
        return True if self.position_id else False

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    @staticmethod
    def reset_password(new_password):
        # TODO 重置密码
        # password = new_password
        # db.session.commit()
        pass

    def is_admin(self):
        """
        是否是管理员
        """
        return True if self.username == current_app.config['ADMIN'] else False
    
    def is_approver(self):
        """
        是否有审批权限(有审批级别则表示有审批权限,否则无)
        """
        return True if self.level_id else False

    @classmethod
    def get_all_users(cls):
        return cls.query.filter_by().order_by(cls.id).all()

    @property
    def approving_messages(self):
        """
        待审批列表，用于消息提示
        :return:
        """
        from app.view_models.approve import CurrentUserApprovingInfo
        return [CurrentUserApprovingInfo(approving) for approving in self.approvings]

    @property
    def need_report_back_applies(self):
        """
        待销假列表
        :return:
        """
        from app.view_models.apply import UserApplyInfo
        applies = []
        for apply in self.applies:
            approve = apply.approve
            if approve.approve_status == 3 and not apply.actual_back_date:
                applies.append(UserApplyInfo(apply))
        return applies

    def get_all_approver(self):
        """
        获取当前用户需要哪些人授权
        :return:
        [{'section': Section, 'level': Level, 'area': Area, 'xuebu': XueBu}, {'section': Section, 'level': Level, 'area': Area}]
        """
        users = []
        from app.lib.rules import Rule
        rule_list = Rule(self)()
        for rule in rule_list:
            users.extend(User.query.filter_by(**rule).all())
            print(User.query.filter_by(**rule).all())
        return users








    # def get_id(self):
    #     return self.id


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
