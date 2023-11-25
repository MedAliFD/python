from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User


app.route("/")
def home():
    print("home")
    return render_template("index.html")


@app.route("/usersf", methods=["POST"])
def user():
    data = request.form
    User.create(data)
    return redirect("/users")


@app.route("/users")
def display_all():
    all_users = User.get_all()
    return render_template("display_all.html", users=all_users)
