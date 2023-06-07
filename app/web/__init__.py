from flask import Blueprint, url_for

__author__ = 'cabbyw'

web = Blueprint('web', __name__, template_folder='templates')

from app.web import auth
from app.web import index
