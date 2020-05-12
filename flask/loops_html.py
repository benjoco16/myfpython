from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Jomane", "Simon", "Mat", "Charm", "Kuya jet"]
    Title = "List of Names"
    return render_template('index.html', pangalan=names, mt=Title)