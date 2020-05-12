from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(): #index() function you can change this function to whatever you want
    headline = "Hello Mother fucker!"
    return render_template("index.html", myvar=headline) #flask will only look for templates folder

@app.route("/paalam")
def bye():
    headline = "Hello salary goodbye"
    return render_template("index.html", myvar=headline) #use current html to render the infor