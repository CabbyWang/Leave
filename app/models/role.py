from app.models.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey
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

    @classmethod
    def get_all_occupations(cls):
        return cls.query.filter_by().order_by(cls.id).all()


class Section(Base):
    """
    部门/科室/办公室：
    卫勤部、政治工作部、信息科、医工科等
    """
    __tablename__ = 'section'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    is_office = Column(Integer, default=0, comment='是否机关部门/科室 是：1 不是：0')
    parent_id = Column(Integer, ForeignKey('section.id'), nullable=True, comment='办公室所在部门：医疗办所属部门为卫勤部')
    child_sections = relationship('Section', back_populates='parent_section', cascade='all')
    parent_section = relationship('Section', back_populates='child_sections', remote_side=[id])
    area_id = Column(Integer, ForeignKey('area.id'), nullable=True, comment='片区')
    xuebu_id = Column(Integer, ForeignKey('xuebu.id'), nullable=True, comment='学部')
    users = relationship('User', backref='section')

    @classmethod
    def get_all_sections(cls):
        return cls.query.filter_by().order_by(cls.id).all()

    @classmethod
    def get_parent_sections(cls):
        """
        机关部门
        :return: 所有带"部"的section
        """
        return cls.query.filter_by(cls.name.like('%部')).all()


class XueBu(Base):
    """
    学部
    : 骨科学部 烧伤学部
    """
    __tablename__ = 'xuebu'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    users = relationship('User', backref='xuebu')
    sections = relationship('Section', backref='xuebu')

    @classmethod
    def get_all_xuebus(cls):
        return cls.query.filter_by().order_by(cls.id).all()


class Area(Base):
    """
    片区
    : 一个片区包含多个科室，由人力资源维护
    """

    __tablename__ = 'area'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    sections = relationship('Section', backref='area')
    users = relationship('User', backref='area')

    @classmethod
    def get_all_areas(cls):
        return cls.query.filter_by().order_by(cls.id).all()


class Position(Base):
    """
    岗位级别:
    根据所处岗位和部门确定审批流程
    """

    __tablename__ = 'position'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    users = relationship('User', backref='position')

    @classmethod
    def get_all_positions(cls):
        return cls.query.filter_by().order_by(cls.id).all()


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
        return cls.query.filter_by().order_by(cls.id).all()
