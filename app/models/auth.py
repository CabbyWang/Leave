from flask_login import UserMixin
from sqlalchemy.orm import relationship

from flask import current_app
from sqlalchemy.testing import in_

from app import login_manager
from app.models.base import Base, db
from sqlalchemy import Column, String, Integer, ForeignKey, func, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.role import Position
from app.view_models.users import UserInfo


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(100), nullable=True)
    username = Column(String(30), unique=True, nullable=False)
    _password = Column('password', String(110), nullable=False)
    phone_number = Column(String(18))
    id_card_number = Column(String(18))
    status = Column(SmallInteger, default=1)  # 默认为0，人力资源审批后激活，status=1
    # section = relationship('Section', back_populates='users')
    section_id = Column(Integer, ForeignKey('section.id'), nullable=True, comment='科室或部门')
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

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

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
        return [UserInfo(i) for i in cls.query.filter_by().order_by(cls.id).all()]

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
        """
        # TODO 从规则表中取还是写死？from app.models.rule import Rule
        if self.position.name == '护士长':
            # section = self.section  # 科室
            # select * from users where position_id = '岗位id' and section_id = '科室id'
            level_ids = db.session.query(User.level_id).filter(User.section == self.section, User.level_id.in_((2, 3))).all()
            users = [User.query.filter_by(level_id=level_id_tuple[0]).first() for level_id_tuple in level_ids]
            # return UserInfo(user)
            return users
        return []
        # [rule.level_id for rule in rules]
        # 2. 通过规则找到相应的审批人id
        # return [self.query.filter_by(level_id=rule.level_id).filter(User.id != self.id).first().id for rule in rules]

    # def get_all_approver(self):
    #     """
    #     获取当前用户需要哪些人授权
    #     :return:
    #     """
    #     from app.models.rule import Rule
    #     # 1. 获取所有规则 # TODO 规则直接写死？
    #     rules = Rule.query.filter_by(occupation_id=self.occupation_id, section_id=self.section_id,
    #                                  status=1).all()
    #     # [rule.level_id for rule in rules]
    #     # 2. 通过规则找到相应的审批人id
    #     # TODO 只获取一个人?
    #     return [self.query.filter_by(level_id=rule.level_id).filter(User.id != self.id).first().id for rule in rules]



    # def get_id(self):
    #     return self.id


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
