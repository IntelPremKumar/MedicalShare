from enum import unique
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '183jhr982f9wet782f3t792tgui'
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    username= db.Column(db.String(20),unique=True, nullable=False)
    password= db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.password}')"



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/enter")
def enter():
    return render_template("profile.html")

@app.route("/signup")
def signup():
    return render_template("signup-p.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/basic")
def basic():
    return render_template("basic.html")

@app.route("/BloodReport")
def BloodReport():
    return render_template("BloodReport.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

@app.route("/observation")
def observation():
    return render_template("observation.html")

if __name__ == "__main__":
    app.run(debug=True, )