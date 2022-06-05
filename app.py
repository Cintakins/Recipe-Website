
# task_manager walk-through code
import os
import random
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# task_manager walk-through code
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# initializing database
mongo = PyMongo(app)


@app.route("/")
@app.route("/get_home")
def get_home():
    recipes = mongo.db.recipes.find()
    recipes_list = []
    for recipe in recipes:
        recipes_list.append(recipe)
    todays_recipe = random.choice(recipes_list)
    return render_template("home.html", todays_recipe=todays_recipe)


@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)

@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            username_input = request.form.get("username").lower()
            existing_username = mongo.db.users.find_one({"username": username_input})
        except:
            print("Error accessing the database")

        if existing_username:
            password_input = request.form.get("password")
            if check_password_hash(existing_username["password"], password_input):
                session["current_user"] = username_input
                full_name = existing_username["first_name"] + " " + existing_username["last_name"]
                flash(f"Welcome back {full_name.title()}")

            else:
                flash("Whoops! Incorrect username or password.")
                return redirect(url_for("login"))

        else:
            flash("Whoops! Incorrect username or password.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

    # using names may result in 2 identical users, but wanted to use name for recipe credit. chose to add both.

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm = request.form.get("confirm_password")
        
        if password == confirm:
            register = {
                "username": request.form.get("username").lower(),
                "first_name": request.form.get("first_name").lower(),
                "last_name": request.form.get("last_name").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

            session["user"] = request.form.get("username").lower()
            flash("Registration successful")

        else:
            flash("Passwords do no match. Try again")
            return redirect(url_for("register"))
    return render_template("register.html")


# code from task-manager min project
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)