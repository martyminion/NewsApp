import urllib.request,json
from .models import Source,Articles

#Getting the API Key
api_key = None
#getting the base url
base_url = None

def configure_request(app):
  '''
  function to get the api key and the base url
  '''
  global api_key,base_url,sources_base_url,search_base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']
  sources_base_url = app.config['NEWS_API_SOURCES_BASE_URL']
  search_base_url = app.config['NEWS_SEARCH_API']

def process_results(news_results):
  '''
  processes the results and transforms them into a list

  args 
  news_results: a dictionary containing source details

  returns
  a list of source objects
  '''

  p_results = []

  for source_item in news_results:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    category = source_item.get('category')
    
    source_object = Source(id,name,description,category)
    p_results.append(source_object)

  return p_results


def get_sources():
  '''
  function that get the json response from our url request
  '''
  source_base_url = sources_base_url.format(api_key)

  with urllib.request.urlopen(source_base_url) as url:
    sources_data = url.read()
    sources_response = json.loads(sources_data)

    source_results = None

    if sources_response['sources']:
      source_results_list = sources_response['sources']
      source_results = process_results(source_results_list)
  return source_results

def process_articles(article_list):
  '''
  function that processes results and returns a list
  '''
  article_result_list = []
   
  for article in article_list:
    author = article.get('author')
    title = article.get('title')
    descriptions = article.get('description')
    publishedAt = article.get('publishedAt')
    url = article.get('url')
    if article.get('content'):
      content = article.get('content')
    else:
      content = "There's isn't much to see here, so visit the site for more"
    if article.get('urlToImage'):
      urltoImage = article.get('urlToImage')
    else:
      urltoImage = "no image"

    article_object = Articles(author,title,descriptions,publishedAt,url,content,urltoImage)
    article_result_list.append(article_object)
  return article_result_list


def get_source_articles(source_id):
  '''
  function that gets the articles from the different sources/ or the selcted source)
  '''
  article_url = base_url.format("everything",source_id,api_key)
  with urllib.request.urlopen(article_url) as url:
    article_data = url.read()
    article_response = json.loads(article_data)

    if article_response['articles']:
      article_list = article_response['articles']
      article_sources = process_articles(article_list)
    
    return  article_sources
  
def get_searched_articles(source_id,search_term):
  '''
  function that gets the articles from a search from a particular news source
  '''
  search_url = search_base_url.format(source_id,search_term,api_key)
  with urllib.request.urlopen(search_url) as url:
    search_data = url.read()
    search_response = json.loads(search_data)


  if search_response['articles']:
    search_list = search_response['articles']
    searched_articles_list = process_articles(search_list)
   
  return  searched_articles_list
    
    