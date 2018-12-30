from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.API.v1.views.user_views import version1 as users
from app.API.v1.views.question_views import version1 as question
from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app= Flask(__name__)
    app.register_blueprint(users)
    app.register_blueprint(question)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('/home/alvin/StackOverflow-lite/config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app
