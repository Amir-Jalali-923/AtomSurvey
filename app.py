from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from helpers import *
from cs50 import SQL

# Initialize Flask application
app = Flask(__name__)

# Connect to SQLite database
db = SQL('sqlite:///AtomSurvey.db')

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Route for the home page
@app.route('/')
def index():
    # Check if user is logged in
    if "user_id" in session:
        # Render homepage with logout options for logged-in users
        return render_template("index.html", name=session["username"], options=logoutOptions, Moptions=logoutOptionsMobile)
    # Render homepage with login options for guests
    return render_template("index.html", options=loginOptions, Moptions=loginOptionsMobile)

# Route for the login page
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # Render login page on GET request
        return render_template("Login.html")
    else:
        # Handle login form submission
        rows = db.execute("SELECT * FROM users WHERE Gcode = ? and pass = ?", request.form.get("Gcode"), hash(request.form.get("pass")))
        if len(rows) != 1:
            # Invalid Gcode or password
            return render_template("error.html", errtext="invalid Gcode or password", errcode="403"), 403
        # Log in the user
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]
        return redirect("/")

# Route for the signup page
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        # Render signup page on GET request
        return render_template("signUp.html")
    else:
        # Handle signup form submission
        rf = request.form

        # Validate form data
        if not rf.get("name") or not rf.get("email") or not rf.get("Gcode") or not rf.get("pass") or not rf.get("pass-con"):
            return render_template("error.html", errtext="incomplete data", errcode="400"), 400

        if rf.get("pass") != rf.get("pass-con"):
            return render_template("error.html", errtext="password confirmation doesn't match with password", errcode="400"), 400

        if not check_email(rf.get("email")):
            return render_template("error.html", errtext="email invalid", errcode="400"), 400

        if not check_Gcode(rf.get("Gcode")):
            return render_template("error.html", errtext="Gcode invalid", errcode="400"), 400

        # Check if Gcode already exists
        rows = db.execute("SELECT * FROM users WHERE Gcode = ?", rf.get("Gcode"))
        if len(rows) > 0:
            return render_template("error.html", errtext="a user with this Gcode already exists", errcode="400"), 400

        # Insert new user into the database
        db.execute("INSERT INTO users(username, email, Gcode, pass) VALUES(?, ?, ?, ?)", rf.get("name"), rf.get("email"), rf.get("Gcode"), hash(rf.get("pass")))
        return redirect("/")

# Route for logging out
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return redirect('/')

# Route for the settings page
@app.route('/Setting', methods=["GET", "POST"])
def setting():
    if not "user_id" in session:
        return redirect('/login')

    if request.method == "GET":
        # Render settings page on GET request
        return render_template("Setting.html")
    else:
        # Handle settings form submission
        rf = request.form

        # Validate form data
        if not rf.get("pass") or not rf.get("pass-con") or not rf.get("currentPass"):
            return render_template("error.html", errtext="incomplete data", errcode="400"), 400

        if rf.get("pass") != rf.get("pass-con"):
            return render_template("error.html", errtext="password confirmation doesn't match with password", errcode="400"), 400

        # Check current password
        rows = db.execute("SELECT * FROM users WHERE id = ? AND pass = ?", session["user_id"], hash(rf.get("currentPass")))
        if len(rows) != 1:
            return render_template("error.html", errtext="incorrect password", errcode="400"), 400

        # Update the password
        db.execute("UPDATE users SET pass = ? WHERE id = ?", hash(rf.get("pass")), session["user_id"])
        return redirect('/')

# Route for the About Us page
@app.route('/AboutUs')
def AboutUs():
    return render_template("AboutUs.html")

# Route for the Contact page
@app.route('/Contact')
def Contact():
    return render_template("Contact.html")


@app.route('/survey', methods=['GET', 'POST'])
def survay():
    if(session['participated']):
        return render_template('error.html', errtext="you have taken this survay before", errcode=400), 400

    if request.method == 'GET':
        session['qn'] = 1
        session['answers'] = {}
    else:
        session['answers'][session['qn']] = request.form.get('answer')
        print(session['answers'])
        session['qn'] += 1
        if session['qn'] > 10:
            return redirect('/save')

    question = get_question('data/questions.csv', session['qn'])
    if not question:
        return render_template('error.html', errtext="no Such Question exists.", errcode=400), 400
    if(question['type'] == '1'):
        return render_template('multipleAnswer.html', title=question['title'], options=['عالی', 'خوب', 'متوسط', 'ضعیف'], qn=session['qn'])
    
    if(question['type'] == '2'):
        return render_template('multipleAnswer.html', title=question['title'], options=['بله', 'خیر'], qn=session['qn'])
    
    if(question['type'] == '3'):
        return render_template('starQuestion.html', title=question['title'], qn=session['qn'])
    
    else:
        return render_template('error.html', errtext="WHAT ARE YOU  DOING HERE ?", errcode=500),500
    

@app.route('/save')
def save():
    if(write_stats("data/answers.json", session['answers']) != 0):
        return render_template("error.html", errtext="OOPS, somthing went wrong, yor response wont be saved!", errcode=400), 400
    session['participated'] = True
    return("your response saved succefuly!\nThank you for your feedBack")

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
