import os
import jwt
from app.API.v1.models.model import users
from flask import jsonify, request
from functools import wraps


key= os.getenv('SECRET_KEY')


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
