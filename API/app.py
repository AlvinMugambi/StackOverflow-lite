import json
from model import users, verify_user_record, verify_user_email,questions
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash


app= Flask(__name__)

app.config['SECRET_KEY']= 'thisissecret'




if __name__ == '__main__':
    app.run(debug=True)
