from flask import Flask, jsonify, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def api(): 
    return {"up": True}

@app.route('/analyse', methods = ['POST'])
def analyse():
    if request.method == 'POST':
        user_req = request.form['user_data']
        data_req = request.form['input_data']
    
    return {"response": "data goes here"}

if __name__ == '__main__':
    app.run()