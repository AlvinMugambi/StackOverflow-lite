import json
from model import users, verify_user_record, verify_user_email,questions
from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash


app= Flask(__name__)

app.config['SECRET_KEY']= 'thisissecret'

# MY DECORATORS

    # decorator where a user requires a token to view
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token= None
        if 'x-access-token' in request.headers:
            token= request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing!'}),401

        try:
            data= jwt.decode(token, app.config['SECRET_KEY'])
            current_user= None
            for user in users:
                if user['public_id'] == data['public_id']:
                    current_user= user

        except:
            return jsonify({'message':'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)
    return decorated


# MY ROUTES
    # register/add a user

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


# authenticate login and create token
@app.route('/login', methods=['POST'])
def login():
    password = request.get_json()['password']
    username = request.get_json()['name']
    response = None

    if not password or not username:
        # if field(s) are empty
        response = jsonify({"error": "Name and email fiels required"})
        # response.status_code = 400
        return response, 400

    reg_user = verify_user_record(username, password)

    # print("USER >> ", user)
    for user in users:
        public_id= user['public_id']
    if reg_user == "Doesn't exist":
        return jsonify({"message": "Please Register first"}), 404

    token = jwt.encode({'public_id': public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm='HS256')

    return jsonify({'token': token.decode('UTF-8')})

if __name__ == '__main__':
    app.run(debug=True)
