from flask import Blueprint

efrain = Blueprint('efrain',__name__, template_folder='templates')

from . import routes