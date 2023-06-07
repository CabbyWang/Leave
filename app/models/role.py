from app.models import db
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


# section = Column()
#     level = Column()
#     occupation = Column()

class Section(db.Model):
    """
    部门：
    卫勤部、政治工作部、信息科、医工科等
    """
    __tablename__ = 'section'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    users = relationship('User', backref='section', lazy='dynamic')


class Level(db.Model):
    """
    级别：判断是否有审批权限和具体什么权限
    中心主管、医学部主任、副主任等
    """
    __tablename__ = 'level'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    # users = relationship('User')
    users = relationship('User', backref='level', lazy='dynamic')


class Occupation(db.Model):
    """
    人员类别：
    聘用、职工、文职、军人等
    """
    __tablename__ = 'occupation'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    users = relationship('User', backref='occupation', lazy='dynamic')
