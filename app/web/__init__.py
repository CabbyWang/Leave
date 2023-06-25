from flask import Blueprint, url_for

__author__ = 'cabbyw'

web = Blueprint('web', __name__, template_folder='templates')

from app.web import index
from app.web import auth
from app.web import leave
from app.web import approve
from app.web.admin import admin
from app.web.admin import level
from app.web.admin import vehicle
from app.web.admin import section
from app.web.admin import occupation
from app.web.admin import rule
from app.web.admin import users
# from app.web.approve import approve
