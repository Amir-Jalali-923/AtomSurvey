from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from hashlib import sha256
from helpers import hash
from cs50 import SQL;

app = Flask(__name__)
db = SQL('sqlite:///AtomSurvey.db')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        rows = db.execute("SELECT * FROM users WHERE Gcode = ? and pass = ?", request.form.get("Gcode"), hash(request.form.get("pass")))
        return render_template("index.html", user=rows)
    
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        



if __name__ == "__main__":
    app.run(debug=True)
