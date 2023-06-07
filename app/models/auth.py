from flask_login import UserMixin
from sqlalchemy.orm import relationship

from app import db, login_manager
# from app.models import Base
from app.models.role import Section, Level, Occupation
from sqlalchemy import Column, String, Integer, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash


# class User(UserMixin, Base):
class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    _password = Column('password', String(100), nullable=False)
    phone_number = Column(String(18))
    id_card_number = Column(String(18), unique=True, nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'), nullable=True)
    section = relationship('Section')
    level_id = Column(Integer, ForeignKey('level.id'), nullable=True)
    level = relationship('Level')
    occupation_id = Column(Integer, ForeignKey('occupation.id'), nullable=True)
    occupation = relationship('Occupation')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

# @login_manager.user_loader
# def get_user(uid):
#     return User.query.get(int(uid))
