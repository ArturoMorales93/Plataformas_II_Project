from flask import render_template
from . import arturo

@arturo.route('/arturo', methods=['GET'])
def arturo():
    return render_template('index_arturo.html')