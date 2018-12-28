from flask import Flask, Blueprint
from app.API.v1.views.user_views import version1 as users
from app.API.v1.views.question_views import version1 as questions

def create_app():
    app = Flask(__name__)
    app.register_blueprint(users)
    app.register_blueprint(questions)

    return app
