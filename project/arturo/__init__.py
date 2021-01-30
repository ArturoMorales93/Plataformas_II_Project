from flask import Blueprint

arturo = Blueprint('arturo',__name__, template_folder='templates')

from . import routes