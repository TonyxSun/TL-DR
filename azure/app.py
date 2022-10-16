from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def api(): 
    return {"up": True}

@app.route('/v1')
def main(): 
    return {"v1": True}

if __name__ == '__main__':
    app.run()