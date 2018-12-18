import json
import datetime
import jwt
from functools import wraps
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from app.API.v1.models.model import users, verify_user_record, verify_user_email, questions, answers
from .. import version1
from app.API.v1.utils.validators import token_required


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


    # a user can view all Questions
@version1.route('/questions', methods=['GET'])
def get_all_questions():
    return jsonify({'Questions':questions}), 201



    # a user can search for a specific question:
@version1.route('/questions/<int:question_id>', methods= ['GET'])
def find_question(question_id):

    clicked_question = None
    for question in questions:
        if question['id'] == question_id:
            clicked_question= question
    if not clicked_question:
        return "message=Question with id {} not found".format(question_id)

    return jsonify({"Question" :clicked_question}),201



    # a registered user can post an answer to a question
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
                    "Answer_id":answer_id}
            question['Answers'].append(answer)
            my_qn = question

    return jsonify({'result':my_qn}), 201


    # a registered user cam delete a question
@version1.route('/questions/<int:question_id>',methods=['DELETE'])
@token_required
def delete_question(current_user,question_id):

    for question in questions:
        if question_id in question.values():
            questions.remove(question)

    return jsonify({'Message':'Deleted succesfully'}), 201


@version1.route('/questions/<questionId>/answers/<answerId>', methods=['PUT'])
def mark_answer():

    
    pass
