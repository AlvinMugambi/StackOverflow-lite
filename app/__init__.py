from app.API.v1.views.user_views import version1 as users
from app.API.v1.views.question_views import version1 as question
from flask import Flask, Blueprint
from config import app_config

def create_app(config_name):
    app= Flask(__name__)
    # app.config.from_object(app_config[config_name])s
    app.register_blueprint(users)
    app.register_blueprint(question)
    return app
