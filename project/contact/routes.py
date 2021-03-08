from flask import render_template
from . import contact

@contact.route('/es/contactenos', methods=['GET'])
@contact.route('/contactenos', methods=['GET'])
def es_contact():
    # Especificar el tema en la variable
    title = "Contáctenos"
    return render_template('es_contact.html', title=title)


@contact.route('/en/contact-us', methods=['GET'])
def en_contact():
    # Especificar el tema en la variable
    title = "Contact us"
    return render_template('en_contact.html', title=title)