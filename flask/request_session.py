from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = [] #create empty array

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        note = request.form.get("note") #Get the input value from html file
        notes.append(note) #Append to loop for note in notes {{note}}

    return render_template("session_one.html", notes=notes)