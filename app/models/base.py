# from datetime import datetime
from contextlib import contextmanager
from datetime import datetime

# from sqlalchemy import Column, Integer, SmallInteger
from flask import current_app
# from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer
from sqlalchemy.orm.query import Query as _Query
from flask_migrate import Migrate

__all__ = ['db', 'Base']
# __all__ = ['db']


# class SQLAlchemy(_SQLAlchemy):
#     @contextmanager
#     def auto_commit(self, throw=True):
#         try:
#             yield
#             self.session.commit()
#         except Exception as e:
#             self.session.rollback()
#             current_app.logger.exception('%r' % e)
#             if throw:
#                 raise e


class Query(_Query):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


# class BaseMixin(object):
#     def __getitem__(self, key):
#         return getattr(self, key)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)


class BaseNoCreateTime(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
