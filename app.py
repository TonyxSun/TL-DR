from flask import Flask, jsonify, redirect, url_for, request
from src.setup import setup
from src.account import create
from dotenv import load_dotenv
load_dotenv()
import os

# from src.auth import main as temp
# import token from .env -> `os.environ.get("api-token")`

app = Flask(__name__)

@app.route('/')
def api(): 
    return {"up": True}

@app.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        user_email = request.form['user_email']
        user_password = request.form['user_password']
        user_phone = request.form['user_phone']
    create(email=user_email, password=user_password, phone_number=user_phone)
    

@app.route('/analyse', methods = ['POST'])
def analyse():
    if request.method == 'POST':
        user_req = request.form['user_data']
        data_req = request.form['input_data']
    
    return {"response": "data goes here"}

if __name__ == '__main__':
    setup()
    app.run()