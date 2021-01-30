from flask import Blueprint

carlos = Blueprint('carlos',__name__, template_folder='templates')

from . import routes