import os
from urllib import parse


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    PASSWORD = 'Change_me@123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:{}@localhost/leave'.format(parse.quote(PASSWORD))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_SECRET_KEY = 'IT 666 to 709 kill pic'
    WTF_CSRF_CHECK_DEFAULT = False

    PAGINATION_PER_PAGE = 10

    ADMIN = 'admin'
    DEBUG = True
