from flask import Blueprint

dixiana = Blueprint('dixiana',__name__, template_folder='templates')

from . import routes