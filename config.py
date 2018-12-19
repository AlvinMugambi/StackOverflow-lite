import os

class config(object):

    DEBUG= False
    TESTING= False

class Development(config):
    DEBUG= True
    TESTING= True

class Testing(config):
    TESTING= True
    DEBUG= True

class Production(config):
    DEBUG= False
    TESTING= False

app_config= {
    "development": Development,
    "testing":Testing,
    "production":Production
}
