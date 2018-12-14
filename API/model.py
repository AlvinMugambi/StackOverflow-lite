from flask import Flask, request, jsonify


users= []
questions= []


def verify_user_email(email):
    verified_email = None
    for user in users:
        if email == user["email"]:
            return 'Email already taken!'
        verified_email= email
    return verified_email
