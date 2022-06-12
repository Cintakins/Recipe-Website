
# task_manager walk-through code
import os
import datetime
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


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# initializing database
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    date = datetime.datetime.now()
    day = date.strftime("%A")

    recipes = mongo.db.recipes.find()
    recipes_list = []
    for recipe in recipes:
        recipes_list.append(recipe)
    todays_recipe = random.choice(recipes_list)
    return render_template("home.html", todays_recipe=todays_recipe, recipes=recipes, day=day)


@app.route("/all_recipes")
def all_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/one_recipe/<recipe_id>")
def one_recipe(recipe_id):
    clicked_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("one_recipe.html", clicked_recipe=clicked_recipe)


@app.route("/search", methods=["POST", "GET"])
def search():
    search_item = request.form.get("search")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": search_item}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/edit/<recipe_id>", methods=["POST", "GET"])
def edit(recipe_id):
    if request.method == "POST":
        recipe_dict = {
            "recipe_name": request.form.get("recipe_name").lower(),
            "category_name_1": request.form.get("category_name_1"),
            "category_name_2": request.form.get("category_name_2"),
            "ingredients": request.form.get("ingredients").lower(),
            "instructions": request.form.get("instructions"),
            "description": request.form.get("description"),
            "img_url": request.form.get("img_url")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)},recipe_dict)
    flash("Recipe Updated!")
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit.html", recipe=recipe)


@app.route("/delete/<recipe_id>")
def delete(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe has been deleted.")
    return redirect("recipes.html")


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
                return redirect(url_for("profile", user=session["current_user"]))

            else:
                flash("Whoops! Incorrect username or password.")
                return redirect(url_for("login"))

        else:
            flash("Whoops! Incorrect username or password.")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/log_out")
def log_out():
    session.clear()
    flash("You have logged out")
    return redirect(url_for("home"))


@app.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):
    recipes = mongo.db.recipes.find()

    user = mongo.db.users.find_one(
        {"username": session["current_user"]})["username"]
    return render_template("profile.html", user=user, recipes=recipes)

    if session["current_user"]:
        return render_template("profile.html", user=user)
    else:
        return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

    # using names may result in 2 identical users, but wanted to use name for recipe credit. chose to add both.

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    
        if existing_user:
            flash("Username taken. Try another")
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

        else:
            flash("Passwords do no match. Try again")
            return redirect(url_for("register"))

        mongo.db.users.insert_one(register)

        session["current_user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for("profile", user=session["current_user"]))

    return render_template("register.html")


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        ingredients = []
        chips = request.form.get("ingredients")
        for chip in chips:
            ingredients.append(chip)
        
        recipe = {
            "recipe_name": request.form.get("recipe_name").lower(),
            "category_name_1": request.form.get("category_name_1"),
            "category_name_2": request.form.get("category_name_2"),
            "ingredients": ingredients,
            "instructions": request.form.getlist("instructions"),
            "description": request.form.get("description"),
            "added_by": session["current_user"],
            "img_url": request.form.get("img_url")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe has been successfully added. Yummy!")
        return redirect(url_for("all_recipes"))
    return render_template("add.html")
        

@app.route("/login_to_add", methods=["POST", "GET"])
def login_to_add():
    flash("You must log in to add a recipe")
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
                return redirect(url_for("add"))

            else:
                flash("Whoops! Incorrect username or password.")
                return redirect(url_for("login_to_add"))

        else:
            flash("Whoops! Incorrect username or password.")
            return redirect(url_for("login_to_add"))
    return render_template("login_to_add.html")


# code from task-manager min project
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)