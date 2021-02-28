from flask import render_template
from . import arturo

@arturo.route('/machine-learning', methods=['GET'])
def arturo():
    # Especificar el tema en la variable
    title = "Machine Learning"
    return render_template('machine-learning.html', title=title)