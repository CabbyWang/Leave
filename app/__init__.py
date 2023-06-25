from flask import Flask
from flask_login import LoginManager
from flask_wtf import CSRFProtect

from .config import Config
from app.models.base import db
# from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
# from flask_wtf.csrf import CSRFProtect


login_manager = LoginManager()
# cache = Cache(config={'CACHE_TYPE': 'simple'})
# limiter = Limiter()


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app(config=None):
    app = Flask(__name__)

    #: load default configuration
    # app.config.from_object('app.settings')
    # app.config.from_object('app.secure')
    app.config.from_object(Config)

    # 注册SQLAlchemy
    db.init_app(app)
    migrate = Migrate(app, db)
    # Bootstrap(app)

    # 注册login模块
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    # 注册flask-cache模块
    # cache.init_app(app)

    # 注册CSRF保护
    # csrf = CSRFProtect()
    # csrf.init_app(app)

    # register_api_blueprint(app)
    register_web_blueprint(app)

    # if config is not None:
    #     if isinstance(config, dict):
    #         app.config.update(config)
    #     elif config.endswith('.py'):
    #         app.config.from_pyfile(config)
    return app
