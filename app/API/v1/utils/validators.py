import os
import re
import jwt
from app.API.v1.models.model import users
from flask import jsonify, request, abort, make_response
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash



key= os.getenv('SECRET_KEY')

    # MY DECORATORS

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token= None
        if 'x-access-token' in request.headers:
            token= request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing!'}),401

        try:
            data= jwt.decode(token, key)
            current_user= None
            for user in users:
                if user['public_id'] == data['public_id']:
                    current_user= user

        except:
            return jsonify({'message':'Token is expired or invalid'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

    # HELPER FUNCTIONS

    # verify a user has input matching passwords and valid passwords
def check_password(password, confirmed_password):
        # check if password meets required length
    if (len(password)<6) or (len(password)>12):
        abort (make_response()),400
        abort(make_response(jsonify(message="Password should not be less than 6 characters or exceed 12"), 400))

    # check if password contains at least an alphabet(a-z)
    if not re.search("[a-z]", password):
        abort(make_response(jsonify(message="Password should contain a letter between a-z"),400))

    # check if password contains at least an upper case letter
    if not re.search("[A-Z]", password):
        abort(make_response(jsonify(message="Password should contain a capital letter"),400))

    # check if password contains at least a number(0-9)
    if not re.search("[0-9]", password):
        abort(make_response(jsonify(message="Password should contain a number(0-9)"),400))

    # Checks if passwords provided by the users match
    if password != confirmed_password:
        abort(make_response(jsonify(message="Passwords do not match!"), 400))

    # If they match..
    hashed_password = generate_password_hash(password, method= 'sha256')

    return hashed_password

    # verify user has input a valid email
def validate_email(email):
    # check if the email is a valid email and if it is already in use
    for user in users:
        if email in user.values():
            abort(make_response(jsonify(Message="Email already taken!"),400))
    try:
        user, domain = str(email).split("@")
    except ValueError:
        abort(make_response(jsonify(message="Invalid Email"), 400))
    if not user or not domain:
        abort(make_response(jsonify(message="Invalid Email"),400))

    # Check that domain is valid
    # valid domain has valid part before and after '.'
    try:
        dom_1, dom_2 = domain.split(".")
    except ValueError:
        abort(make_response(jsonify(message="Invalid Email"),400))
    if not dom_1 or not dom_2:
        abort(make_response(jsonify(message="Invalid Email"),400))

    return email

    # verify a user is in the db
def verify_user_records(email,password):
    # verifies if the entered data is contained in the database to verify login
    verified= None
    for user in users:
        if email not in user.values() or password not in user.values():
            abort(make_response(jsonify(message= "Please Register First" ), 400))

        verified= user

    return verified
