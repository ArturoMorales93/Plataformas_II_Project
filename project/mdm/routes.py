from flask import render_template
from . import mdm

@mdm.route('/en/mdm', methods=['GET'])
@mdm.route('/mdm', methods=['GET'])
def mdm():
    return render_template('Master_Data_Management.html')
