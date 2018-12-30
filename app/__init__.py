from flask import Flask, Blueprint
from config import app_config
from app.API.v1.views.user_views import version1 as users
from app.API.v1.views.question_views import version1 as questions

def create_app(config):
    app = Flask(__name__)
    app.register_blueprint(users)
    app.register_blueprint(questions)
    app.config.from_object(app_config[config])

    return app
