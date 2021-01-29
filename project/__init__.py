from flask import Flask

from .index import index

app = Flask(__name__)
app.config.from_pyfile('config/config.cfg')
app.register_blueprint(index)