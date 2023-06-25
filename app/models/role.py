from app.models.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Occupation(Base):
    """
    人员类别：
    聘用、职工、文职、军人等
    """
    __tablename__ = 'occupation'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    users = relationship('User', backref='occupation')
    # users = relationship('User', backref='occupation', lazy='dynamic')

    @classmethod
    def get_all_occupations(cls):
        # {1: '聘用', 2: '文职'}
        return {a.id: a.name for a in cls.query.filter_by().order_by(cls.id).all()}


class Section(Base):
    """
    部门：
    卫勤部、政治工作部、信息科、医工科等
    """
    __tablename__ = 'section'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    users = relationship('User', backref='section')

    @classmethod
    def get_all_sections(cls):
        # {1: '卫勤部', 2: '信息科'}
        return {a.id: a.name for a in cls.query.filter_by().order_by(cls.id).all()}


class Position(Base):
    """
    岗位级别:
    根据所处岗位和部门确定审批流程
    """

    __tablename__ = 'position'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    users = relationship('User', backref='position')
    pass


class Level(Base):
    """
    审批级别：和岗位级别类似，但是用于确定审批权限
    中心主管、医学部主任、副主任等
    """
    __tablename__ = 'level'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    users = relationship('User', backref='level')
    # users = relationship('User', backref='level', lazy='dynamic')

    @classmethod
    def get_all_levels(cls):
        # {1: '中心领导', 2: '普通'}
        return {a.id: a.name for a in cls.query.filter_by().order_by(cls.id).all()}
