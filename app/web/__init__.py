import datetime

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
from app.web.admin import area
from app.web.admin import xuebu
from app.web.admin import position
# from app.web.approve import approve


@web.context_processor
def inject_current_hour():
    return {"current_hour": datetime.datetime.now().hour}


# @web.context_processor
# def inject_current_time():
#     return {"current_time": datetime.datetime.now().time()}
