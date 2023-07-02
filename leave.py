# from app import app
"""
Created by cabbyw on 2023/06/04
"""
from app import create_app
from app.models import db
from app.models.base import Base


__author__ = 'cabbyw'

app = create_app()


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
