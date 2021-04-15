from flask import Flask
from flask_googletrans import translator

from .index import index
from .dixiana import dixiana
from .efrain import efrain
from .landia import landia
from .arturo import arturo
from .carlos import carlos
from .about import about
from .mdm import mdm

app = Flask(__name__)
app.config.from_pyfile('config/config.cfg')
ts = translator(app=app, cache=True, fail_safe=False, service_urls=['translate.googleapis.com','translate.google.com','translate.google.co.kr'])

app.register_blueprint(index)
app.register_blueprint(dixiana)
app.register_blueprint(efrain)
app.register_blueprint(landia)
app.register_blueprint(arturo)
app.register_blueprint(carlos)
app.register_blueprint(about)
app.register_blueprint(mdm)