from flask import Flask, Blueprint,request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.API.v1.views.user_views import version1 as users
from app.API.v1.views.question_views import version1 as question
from instance import config

db = SQLAlchemy()

def create_app(config_name):
    app= Flask(__name__)
    app.register_blueprint(users)
    app.register_blueprint(question)
    # app.config.from_object(app_config[config_name])
    app.config.from_object('instance.config.{}'.format(config_name))
    app.config.from_pyfile('/home/alvin/StackOverflow-lite/instance/config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/api/v2/questions', methods = ['POST'])
    def post_question():
        q= str(request.data.get('Question'))
        t= str(request.data.get('Title'))
        if question:
            question= Question(question=q)
            title= Question(title=t)
            question.save()
            title.save()
            response= jsonify({'id': question.id,
                                'Title':title.title,
                                'Question':question.question})
            response.status_code= 201
            return response

    @app.route('/api/v2/questions', methods= ['GET'])
    def get_questions():
        questions= Question.get_all()
        result= []

        for question in questions:
            q = {'id':question.id,
                'title':question.title,
                'question':question.question}
            result.append(q)
        response= jsonify(result)
        response.status_code= 200
        return response


    return app
