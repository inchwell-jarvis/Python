from flask import Blueprint

index_bp = Blueprint('index_bp', __name__)


@index_bp.route('/index')
def index():
    return {'name': '123'}


@index_bp.route('/index2')
def index2():
    return 'Index index2'
