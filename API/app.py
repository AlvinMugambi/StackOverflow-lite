import json
from model import users, verify_user_record, verify_user_email,questions
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash


app= Flask(__name__)

app.config['SECRET_KEY']= 'thisissecret'

@app.route('/register', methods=['POST'])
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
        'public_id':public_id
        }
    users.append(user)

    return jsonify({'User':users}), 201

@app.route('/login', methods=['POST'])
def login():

if __name__ == '__main__':
    app.run(debug=True)
