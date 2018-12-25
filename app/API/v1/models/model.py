from flask import Flask, request, jsonify


users= []
questions= [{'id':1, 'Question':"initiator?", 'Answers':[]}, ]
answers=[{"Answer": "initiator ans",
        "Answer_id":1,
        "Accepted":False},]



def verify_user_email(email):
    verified_email = None
    for user in users:
        if email == user["email"]:
            return 'Email already taken!'
        verified_email= email
    return verified_email

def verify_user_record(username, password):
    record = None
    for user in users:
        if password in user.values() and username in user.values():
            record = user
            return "exists"

    return "Doesn't exist"
