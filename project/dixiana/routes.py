from flask import render_template
from . import dixiana

@dixiana.route('/dixiana', methods=['GET'])
def dixiana():
    return render_template('index_dixiana.html')