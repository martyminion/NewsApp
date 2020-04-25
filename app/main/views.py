from flask import render_template
from . import main
from ..requests import get_sources

@main.route("/")
def index():
  '''
  returns the index page and its data
  '''
  #Getting the sources
  sources = get_sources()
  title = "Home - News App"

  return render_template('index.html',sources = sources, title = title)