from flask import render_template
from . import arturo
# Especificar el tema en la variable
title = "Machine Learning"

@arturo.route('/machine-learning', methods=['GET'])
def arturo():
    return render_template('machine-learning.html', title=title)