from flask import render_template
from . import landia

@landia.route('/landia', methods=['GET'])
def landia():
    return render_template('index_landia.html')