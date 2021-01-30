from flask import Flask

from .index import index
from .dixiana import dixiana
from .efrain import efrain
from .landia import landia
from .arturo import arturo
from .carlos import carlos

app = Flask(__name__)
app.config.from_pyfile('config/config.cfg')
app.register_blueprint(index)
app.register_blueprint(dixiana)
app.register_blueprint(efrain)
app.register_blueprint(landia)
app.register_blueprint(arturo)
app.register_blueprint(carlos)