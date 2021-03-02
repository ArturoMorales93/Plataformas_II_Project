from flask import render_template
from . import index

@index.route('/', methods=['GET'])
@index.route('/es/', methods=['GET'])
def home():
    return render_template('es_index.html')


@index.route('/en/', methods=['GET'])
def home_english():
    return render_template('en_index.html')