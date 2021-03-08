from flask import Blueprint

quienesSomos = Blueprint('quienesSomos',__name__, template_folder='templates')

from . import routes