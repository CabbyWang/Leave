from datetime import datetime
from app import db
# from app.models.base import Base
from sqlalchemy import Column, Integer, DateTime, String


# class Leave(db.Model):
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, nullable=False)
#     start_time = Column(DateTime, nullable=False)
#     end_time = Column(DateTime, nullable=False)
#     reason = Column(String(255), nullable=False)
#     status = Column(Integer, nullable=False)
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'user_id': self.user_id,
#             'start_time': self.start_time.isoformat(),
#             'end_time': self.end_time.isoformat(),
#             'reason': self.reason,
#             'status': self.status
#         }