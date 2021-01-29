from flask import render_template
from . import index

@index.route('/', methods=['GET'])
def home():
    return render_template('index.html')
