from flask import Blueprint

landia = Blueprint('landia',__name__, template_folder='templates')

from . import routes