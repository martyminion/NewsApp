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
  global api_key,base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']

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
  sources_url = base_url.format("","",api_key)

  with urllib.request.urlopen(sources_url) as url:
    sources_data = url.read()
    sources_response = json.loads(sources_data)

    source_results = None

    if sources_response['sources']:
      source_results_list = sources_response['sources']
      source_results = process_results(source_results_list)
  return source_results