from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Mother Fucker"

@app.route("/tae")
def tae():
    return "Hello tae"


@app.route("/<url_here>")
def ss(url_here):
    url_here = url_here.capitalize()
    return '<center><h1>Hello ' + url_here + "!</h1></center>"