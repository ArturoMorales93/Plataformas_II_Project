from flask import Blueprint

mdm = Blueprint('mdm', __name__, template_folder='templates')

from . import routes