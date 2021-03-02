from flask import render_template
from . import landia

@landia.route('/es/nanotecnologia', methods=['GET'])
@landia.route('/nanotecnologia', methods=['GET'])
def es_landia():
    return render_template('es_index_landia.html')


@landia.route('/en/nanotecnologia', methods=['GET'])
def en_landia():
    return render_template('en_index_landia.html')