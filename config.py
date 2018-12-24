import os
'''Configurations for the app this will allow the set up
    of env variables'''

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    ENV="production"


class Development(Config):
    DEBUG = True
    ENV="development"


class Testing(Config):
    DEBUG = True
    TESTING = True
    ENV="testing"


class Production(Config):
    DEBUG = False
    TESTING = False
    ENV="production"


app_config = dict(
    development=Development,
    testing=Testing,
    production=Production
)
