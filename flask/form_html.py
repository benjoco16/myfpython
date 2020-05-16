from flask import Flask, render_template, request #request is for form route

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method=="GET":
        return "Please Fill Up the form before accessing this Page"
    else:
        name = request.form.get("name")
        return render_template('hello.html', name=name)