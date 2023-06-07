from . import web


@web.route('/hello')
def hello():
    return 'Hello, cabbyw'
