from flask import request, abort, jsonify

def create_app(config_name):
    from api.models.models import Question

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
