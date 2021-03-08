from flask import render_template
from . import quienesSomos

@quienesSomos.route('/es/quienes-somos', methods=['GET'])
@quienesSomos.route('/quienes-somos', methods=['GET'])
def es_quienesSomos():
    # Especificar el tema en la variable
    title = "¿Quiénes somos?"
    return render_template('es_quienes-somos.html', title=title)


@quienesSomos.route('/en/about-us', methods=['GET'])
def en_quienesSomos():
    # Especificar el tema en la variable
    title = "About us"
    return render_template('en_quienes-somos.html', title=title)