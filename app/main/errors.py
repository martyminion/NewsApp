from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourOfour(error):
  '''
  to be used to render the 404 error page, the decorator makes it have a global scope not just within the blueprint
  '''
  return render_template('FourOFour.html'),404