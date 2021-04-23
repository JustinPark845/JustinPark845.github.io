from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/research")
def research():
    return render_template("research.html")