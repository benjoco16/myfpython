from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Mother FUckers sw2"

@app.route("/jom")
def jom():
    return "Hello There Benssssadas das"

@app.route("/benj")
def benj():
    return "Hello There SSS"