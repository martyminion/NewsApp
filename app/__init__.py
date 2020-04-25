from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from .requests import configure_request

bootstrap = Bootstrap()

def create_app(config_name):
  '''
  enables us to create the app under different configurations
  '''
  app = Flask(__name__)

  #creating the app configurations
  app.config.from_object(config_options[config_name])

  #initializing the flask extensions
  bootstrap.init_app(app)

  #registering a blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  #setting the configs
  configure_request(app)
  return app
