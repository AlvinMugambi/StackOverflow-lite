import json
import jwt
from flask import Flask, request, jsonify, make_response
from app.API.v1.models.model import users, questions, answers
from .. import version1
from app.API.v1.utils.validators import token_required

    # A REGISTERED USER CAN POST A QUESTION
@version1.route('/questions',methods=['POST'])
@token_required
def post_question(current_user):

    qn= request.get_json()['Question']
    # if no question is posted
    if not qn:
        return jsonify({"message": "Ask a question"}), 400
    question_id=len(questions)+1
    question={'id':question_id, 'Question':qn, 'Answers':[]}
    # append the question dict to the questions list
    questions.append(question)

    return jsonify({'Your Question':qn}), 201


    # A USER CAN VIEW ALL QUESTIONS
@version1.route('/questions', methods=['GET'])
def get_all_questions():
    return jsonify({'Questions':questions}), 200



    # A USER CAN FETCH A SPECIFIC QUESTION
@version1.route('/questions/<int:question_id>', methods= ['GET'])
def find_question(question_id):

    clicked_question = None
    for question in questions:
        if question['id'] == question_id:
            clicked_question= question
    if not clicked_question:
        return "message=Question with id {} not found".format(question_id)

    return jsonify({"Question" :clicked_question}),200



    # A REGISTERED USER CAN POST AN ANSWER TO A QUESTION
@version1.route('/questions/<int:question_id>/answers', methods=['POST'])
@token_required
def answer_question(current_user,question_id):

    ans= request.get_json()['Answer']

    if not ans:
        return jsonify({"Message":"Please provide an answer"}), 400

    my_qn= None
    answer=None

    answer_id= len(answers)+1

    for question in questions:
        if question_id in question.values():
            answer={"Answer": ans,
                    "Answer_id":answer_id,
                    "Accepted":False}
            question['Answers'].append(answer)
            answers.append(answer)
            my_qn = question

    return jsonify({'result':my_qn}), 201


    # A REGISTERED USER CAN DELETE A QUESTION
@version1.route('/questions/<int:question_id>',methods=['DELETE'])
@token_required
def delete_question(current_user,question_id):

    for question in questions:
        if question_id in question.values():
            questions.remove(question)

    return jsonify({'Message':'Deleted succesfully'}), 200

    # A REGISTERED USER CAN ACCEPT AN ANSWER TO THEIR QUESTION AS THE PREFERRED 0R ACCEPTED ANSWER
@version1.route('/questions/<int:question_id>/answers/<int:answer_id>', methods=['PUT'])
@token_required
def mark_answer(current_user,question_id,answer_id):
    my_question=None
    pref_answer=None

    for question in questions:
        if question_id in question.values():
            my_question=question
    if not my_question:
        return jsonify({"Error":"No question found with that id"}), 400
    for answer in answers:
        if answer_id in answer.values():
            answer['Accepted']=True
            pref_answer=answer

    return jsonify({"Marked answer": pref_answer}), 201
