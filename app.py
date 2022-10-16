from flask import Flask, jsonify, redirect, url_for, request
from src.setup import setup
from src.account import create_user, login_user, request_verify_user
from dotenv import load_dotenv
load_dotenv()
import os
import cohere
import nlp

os.system("curl --create-dirs -o $HOME/.postgresql/root.crt -O https://cockroachlabs.cloud/clusters/02d0901b-5fb2-4a67-b68c-654b2c8c7731/cert")

app = Flask(__name__)
api_key = os.getenv('COHERE_KEY')
co = cohere.Client(api_key)

@app.route('/')
def api(): 
    return {"up": True}

@app.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        content = request.json
        user_email = content['user_email']
        user_password = content['user_password']
        user_phone = content['user_phone']
        
    resp = create_user(email=user_email, password=user_password, phone_number=user_phone)
    return resp

@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        content = request.json
        user_email = content['user_email']
        user_password = content['user_password']

    resp = login_user(email=user_email, password=user_password)
    return resp

@app.route('/request_verify', method = ['POST'])
def request_verify():
    if request.method == 'POST':
        content = request.json
        user_email = content['user_email']
    
    resp = request_verify_user(email=user_email)
    return resp

@app.route('/analyze', methods = ['POST'])
def analyse():
    if request.method == 'POST':
        print(request)
        user_req = request.form['user_data']
        data_req = request.form['input_data']
    
    tldr = nlp.generateSummery(co, data_req)
    # can get other attributes (like sentiment weight)
    sentiment_res = nlp.generateSentiment(co, data_req)
    return {"tldr": tldr, "sentiment": sentiment_res.prediction}

if __name__ == '__main__':
    # setup()
    app.run()
