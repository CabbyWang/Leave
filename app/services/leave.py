from datetime import datetime
from app.models.leave import Leave
from app import db

class LeaveService:
    @staticmethod
    def get_all_leaves():
        leaves = Leave.query.all()
        return [leave.to_dict() for leave in leaves]

    @staticmethod
    def get_leave(id):
        leave = Leave.query.get(id)
        if leave is None:
            return None
        return leave.to_dict()

    @staticmethod
    def create_leave(user_id, start_time, end_time, reason):
        leave = Leave(
            user_id=user_id,
            start_time=datetime.fromisoformat(start_time),
            end_time=datetime.fromisoformat(end_time),
            reason=reason,
            status=0
        )
        db.session.add(leave)
        db.session.commit()
        return leave.to_dict()

    @staticmethod
    def update_leave(id, user_id, start_time, end_time, reason, status):
        leave = Leave.query.get(id)
        if leave is None:
            return None
        leave.user_id = user_id
        leave.start_time = datetime.fromisoformat(start_time)
        leave.end_time = datetime.fromisoformat(end_time)
        leave.reason = reason
        leave.status = status
        db.session.commit()
        return leave.to_dict()

    @staticmethod
    def delete_leave(id):
        leave = Leave.query.get(id)
        if leave is None:
            return False
        db.session.delete(leave)
        db.session.commit()
        return True