from flask import render_template
from . import carlos

@carlos.route('/iot', methods=['GET'])
def carlos():
    return render_template('index_carlos.html')