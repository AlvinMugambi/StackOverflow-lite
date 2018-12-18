import json
import datetime
import jwt
from functools import wraps
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from app.API.v1.models.model import users, verify_user_record, verify_user_email,questions
from .. import version1
from app.API.v1.utils.validators import token_required, key




# MY ROUTES
    # register/add a user

@version1.route('/auth/signup', methods=['POST'])
def create_user():
    user= {}
    name = request.get_json()['name']
    email= request.get_json()['email']
    password=request.get_json()['password']
    public_id=str(uuid.uuid4())

    if not name or not email or not password:
        response = jsonify({"error": "Name, email and password fields required"})
        return response, 400

    new_user= verify_user_email(email)
    print("USER >> ", new_user)

    if new_user == 'Email already taken!':
        return jsonify({'error': 'Email already taken!'})

    hashed_password = generate_password_hash(password,method= 'sha256')

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
    username = request.get_json()['name']
    response = None


    if not password or not username:
        # if field(s) are empty
        response = jsonify({"error": "Name and Password fields required"})
        # response.status_code = 400
        return response, 400

    reg_user = verify_user_record(username, password)

    # print("USER >> ", user)
    for user in users:
        public_id= user['public_id']
    if reg_user == "Doesn't exist":
        return jsonify({"message": "Please Register first"}), 404

    token = jwt.encode({'public_id': public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120)}, key,algorithm='HS256')

    return jsonify({'token': token.decode('UTF-8')})



    # view all users in the database
@version1.route('/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    return jsonify({'users':users}), 200
