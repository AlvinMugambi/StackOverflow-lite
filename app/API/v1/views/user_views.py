import json
import datetime
import jwt
from flask import Flask, request, jsonify, make_response, abort
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from app.API.v1.models.model import users, questions
from .. import version1
from app.API.v1.utils.validators import token_required, key, verify_user_records, validate_email, check_password




# MY ROUTES
    # register/add a user

@version1.route('/auth/signup', methods=['POST'])
def create_user():
    user= {}
    name = request.get_json()['Username']
    email= request.get_json()['Email']
    password=request.get_json()['Password']
    conf_pass= request.get_json()['Confirm Password']
    public_id=str(uuid.uuid4())

    if not username or not email or not password or not conf_pass:
        abort(make_response("All fields are required")), 400

    email= validate_email(email)
    hashed_password=check_password(password,conf_pass)
    print("USER >> ", email)

    # if new_user == 'Email already taken!':
    #     return jsonify({'error': 'Email already taken!'})

    user = {
        'name':name,
        'email':email,
        'password':hashed_password,
        'password':password,
        'public_id':public_id
        }
    users.append(user)

    return jsonify({'Message':'Registered succesfully'}), 201


# authenticate login and create token
@version1.route('/auth/login', methods=['POST'])
def login():
    password = request.get_json()['password']
    email = request.get_json()['Email']
    response = None


    if not password or not email:
        # if field(s) are empty
        response = jsonify({"error": "Name and Password fields required"})
        # response.status_code = 400
        return response, 400

    reg_user = verify_user_records(email,password)

    # print("USER >> ", user)
    for user in users:
        if email in user.values():
            public_id= user['public_id']

    if not reg_user:
        abort(make_response(jsonify(message= "Please Register First" ), 400))

    token = jwt.encode({'public_id': public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120)}, key,algorithm='HS256')

    return jsonify({'token': token.decode('UTF-8')})



    # view all users in the database
@version1.route('/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    return jsonify({'users':users}), 200
