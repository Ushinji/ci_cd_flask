from flask import redirect, render_template
from app import application


@application.route('/', methods=['GET'])
def root_page():
    return render_template('session/index.html')
