from flask import render_template
from . import about

@about.route('/es/quienes-somos', methods=['GET'])
@about.route('/quienes-somos', methods=['GET'])
def es_about():
    # Especificar el tema en la variable
    title = "¿Quiénes somos?"
    return render_template('es_about.html', title=title)


@about.route('/en/about-us', methods=['GET'])
def en_about():
    # Especificar el tema en la variable
    title = "About us"
    return render_template('en_about.html', title=title)