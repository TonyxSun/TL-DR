from flask import Flask, jsonify, redirect, url_for, request
from src.setup import setup
from src.account import create
from dotenv import load_dotenv
load_dotenv()
import os, cohere
import nlp

app = Flask(__name__)
api_key = os.getenv('COHERE_KEY')
co = cohere.Client(api_key)

@app.route('/')
def api(): 
    return {"up": True}

@app.route('/signup', methods = ['POST'])
def signup():
    if request.method == 'POST':
        user_email = request.args['user_email']
        user_password = request.args['user_password']
        user_phone = request.args['user_phone']
    resp = create(email=user_email, password=user_password, phone_number=user_phone)
    return {"response": resp}
    

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
    setup()
    app.run()
