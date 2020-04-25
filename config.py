import os

class Config:
  '''
  carries the base configurations of the app to be inherited by the other cofig options
  '''
  NEWS_API_BASE_URL = 'http://newsapi.org/v2/{}?sources={}&apiKey={}'
  NEWS_API_SOURCES_BASE_URL = 'http://newsapi.org/v2/sources?&apiKey={}'
  NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
  SECRET_KEY=os.environ.get('SECRET_KEY')


class ProdConfig(Config):
  '''
  defines the config options for a production environment and inherits from Config
  '''
  DEBUG = False

class DevConfig(Config):
  '''
  defines the config options for a development environment and inherits from Config
  '''
  DEBUG = True

config_options = {
  'development' :DevConfig,
  'production' :ProdConfig
}