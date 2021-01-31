from flask import render_template
from . import base

@base.route('/base', methods=['GET'])
def base():
    return render_template('base.html')
