from flask import render_template
from . import main
from ..requests import get_sources,get_source_articles

@main.route("/")
def index():
  '''
  returns the index page and its data
  '''
  #Getting the sources
  sources = get_sources()
  title = "Home - News App"

  return render_template('index.html',sources = sources, title = title)

@main.route("/search/<sourceId>")
def topArticles(sourceId):
  '''
  function tht displays the results from a particular source
  '''
  article_results = get_source_articles(sourceId)

  title = f"Articles from {sourceId}"

  return render_template("articles.html",title = title, articles = article_results)