from cs50 import SQL
from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)

db = SQL("sqlite:///users.db")

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if not session.get("username"):
        return redirect("/register")
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    # Validate submission
    if request.method == "POST":
        session["username"] = request.form.get("username")
        username = request.form.get("username")
        password = request.form.get("password")
        
        # create table to store all users' username + pw
        db.execute("CREATE TABLE IF NOT EXISTS users_cred (username TEXT NOT NULL, password TEXT NOT NULL)")
        db.execute("INSERT INTO users_cred (username, password) VALUES(?, ?)", username, password)

        # create table to store each user's website + pw
        db.execute("CREATE TABLE IF NOT EXISTS {username} (website TEXT NOT NULL, password TEXT NOT NULL)".format(username=username))

        return redirect("/homepage")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")

@app.route("/homepage")
def homepage():
    # registrants = db.execute("SELECT * FROM registrants")
    return render_template("home.html", username = session.get("username", "user"))

@app.route("/savedpasswords")
def savedpasswords():
    # registrants = db.execute("SELECT * FROM registrants")
    user_website_pw = db.execute("SELECT * FROM {username}".format(username=session.get("username")))
    return render_template("history.html", username = session.get("username", "user"), user_website_pw = user_website_pw)

@app.route("/savepw", methods= ["GET", "POST"])
def savepw():
    
    # Ensure savedpw exists
    if "savedpw" not in session:
        session["savedpw"] = []
    # POST
    if request.method == "POST":
        username = session.get("username")
        website = request.form.get("website")
        generated_password = request.form.get("hiddenpw")
        if website:
            # db.execute("INSERT INTO {username} VALUES({website}, {generated_password})".format(username=username, website="abc.com", generated_password = generated_password))
            db.execute("INSERT INTO ? VALUES(?, ?)", username, website, generated_password)
            # session["savedpw"].append ([website, generated_password])
        return redirect ("/homepage")
    # GET
    # books = db.execute("SELECT saved_passwords FROM user_creds WHERE username = (?)", session["username"])
    return render_template("history.html", username = session.get("username", "user"))

@app.route("/deletepw", methods= ["GET", "POST"])
def deletepw():
    if request.method == "POST":
        username = session.get("username")
        to_del = request.form.get("to_del_pw")

        if to_del:
            db.execute("DELETE FROM ? WHERE password = ?", username, to_del)
        return redirect ("/savedpasswords")