from flask import render_template
from . import arturo

@arturo.route('/es/machine-learning', methods=['GET'])
@arturo.route('/machine-learning', methods=['GET'])
def es_arturo():
    # Especificar el tema en la variable
    title = "Machine Learning"
    return render_template('machine-learning.html', title=title)


@arturo.route('/en/machine-learning', methods=['GET'])
def en_arturo():
    # Especificar el tema en la variable
    title = "Machine Learning"
    return render_template('en_machine-learning.html', title=title)