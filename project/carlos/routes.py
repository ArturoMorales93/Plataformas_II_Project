from flask import render_template
from . import carlos


@carlos.route('/es/iot', methods=['GET'])
@carlos.route('/iot', methods=['GET'])
def iot_es():
    return render_template('es_iot.html')


@carlos.route('/en/iot', methods=['GET'])
def iot_en():
    return render_template('en_iot.html')
