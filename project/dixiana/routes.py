from flask import render_template
from . import dixiana

@dixiana.route('/es/tecnologia-5g', methods=['GET'])
@dixiana.route('/tecnologia-5g', methods=['GET'])
def es_dixiana():
    return render_template('es_5g.html')


@dixiana.route('/en/tecnologia-5g', methods=['GET'])
def en_dixiana():
    return render_template('en_5g.html')