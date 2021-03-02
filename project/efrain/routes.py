from flask import render_template
from . import efrain

@efrain.route('/es/rpa', methods=['GET'])
@efrain.route('/rpa', methods=['GET'])
def es_efrain():
    return render_template('es_index_efrain.html')


@efrain.route('/en/rpa', methods=['GET'])
def en_efrain():
    return render_template('en_index_efrain.html')