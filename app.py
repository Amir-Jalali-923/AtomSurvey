from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from hashlib import sha256
from helpers import hash, check_email
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
        return redirect("/")
    
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        rf = request.form
        if(not rf.get("name") or not rf.get("email") or not rf.get("Gcode") or not rf.get("pass") or not rf.get("pass-con")):
            return render_template("error.html", errtext="incomplete data", errcode="400"), 400
        elif rf.get("pass") != rf.get("pass-con"):
            return render_template("error.html", errtext="password confirmation doesn't match with password", errcode="400"), 400
        elif not check_email(rf.get("email")):
            return render_template("error.html", errtext="email invalid", errcode="400"), 400


        db.execute("INSERT INTO users(username, email, Gcode, pass) VALUES(?, ?, ?, ?)",
                    rf.get("name"), rf.get("email"), rf.get("Gcode"), hash(rf.get("pass")))
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
