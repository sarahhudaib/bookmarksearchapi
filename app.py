from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def index ():
    return "Hello world"

@app.get('/hello')
def say_hello ():
    return jsonify({"name": "Sarah" ,"message": "Hello world"})