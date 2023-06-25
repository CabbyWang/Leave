from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.view_models.rule import RuleInfo
from app.models.role import Section, Level, Occupation


class Rule(Base):
    """
    审批规则表
    """
    __tablename__ = "rule"

    id = Column(Integer, autoincrement=True, primary_key=True, comment='rule_id')
    section_id = Column(Integer, ForeignKey('section.id'), nullable=True)
    section = relationship('Section')
    position_id = Column(Integer, ForeignKey('position.id'))
    position = relationship('Position')
    level_id = Column(Integer, ForeignKey('level.id'), nullable=True)
    level = relationship('Level')

    @classmethod
    def get_all_rules(cls):
        # RuleInfo
        return [RuleInfo(i) for i in cls.query.filter_by().order_by(cls.id).all()]
