import os
from urllib import parse


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    PASSWORD = 'Change_me@123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:{}@localhost/leave'.format(parse.quote(PASSWORD))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
