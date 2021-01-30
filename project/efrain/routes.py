from flask import render_template
from . import efrain

@efrain.route('/efrain', methods=['GET'])
def efrain():
    return render_template('index_efrain.html')