import os
from app.API.v1.views.user_views import version1 as users
from app.API.v1.views.question_views import version1 as question
from flask import Flask, Blueprint
# from config import config





def create_app():
    app= Flask(__name__)
    app.register_blueprint(users)
    app.register_blueprint(question)
    return app


# version1 = Blueprint("apiv1", __name__, url_prefix="/api/v1")

app= create_app()


if __name__ == '__main__':
        app.run(debug=True)
