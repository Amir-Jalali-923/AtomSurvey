from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from hashlib import sha256
from helpers import hash, check_email, check_Gcode
from cs50 import SQL;

app = Flask(__name__)
db = SQL('sqlite:///AtomSurvey.db')
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    if "user_id" in session:
        return render_template("index.html", user_id=session["user_id"])
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "GET":
        return render_template("login.html")
    else:
        rows = db.execute("SELECT * FROM users WHERE Gcode = ? and pass = ?", request.form.get("Gcode"), hash(request.form.get("pass")))
        if len(rows) != 1:
            return render_template("error.html", errtext="invalid Gcode or password ", errcode="403"), 403
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        rf = request.form

        if(not rf.get("name") or not rf.get("email") or not rf.get("Gcode") or not rf.get("pass") or not rf.get("pass-con")):
            return render_template("error.html", errtext="incomplete data", errcode="400"), 400
        
        if rf.get("pass") != rf.get("pass-con"):
            return render_template("error.html", errtext="password confirmation doesn't match with password", errcode="400"), 400
        
        if not check_email(rf.get("email")):
            return render_template("error.html", errtext="email invalid", errcode="400"), 400
        
        if not check_Gcode(rf.get("Gcode")):
            return render_template("error.html", errtext="Gcode invalid", errcode="400"), 400

        rows = db.execute("SELECT * FROM users WHERE Gcode = ?", rf.get("Gcode"))
        if len(rows) > 0:
            return render_template("error.html", errtext="a user with this Gcode already exists", errcode="400"), 400

        db.execute("INSERT INTO users(username, email, Gcode, pass) VALUES(?, ?, ?, ?)",
                    rf.get("name"), rf.get("email"), rf.get("Gcode"), hash(rf.get("pass")))
        return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
