from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.recipe import Recipe

# =======================================
# Render New Recipe Page
# =======================================


@app.route('/new_recipe')
def new_recipe():
    if "user_id" not in session:
        flash("You have to login or register before entering =( sorry bout that...")
        return redirect("/")

    return render_template("new_recipe.html", user_id=session['user_id'])

# =======================================
# Process Create New Recipe
# =======================================


@app.route('/new_recipe/process', methods=['POST'])
def create_recipe():
    # validate the form data

    # need this condition because if a radio button isn't selected, it doesn't return anything at all, which causes an error when trying to pull it from the form data
    if 'under_30' not in request.form:
        session['under_30'] = None
    else:
        session['under_30'] = request.form['under_30']

    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        # this coming from session! see condition above
        "under_30": session["under_30"],
        "instructions": request.form["instructions"],
        # this is from the hidden input in the form - could also pull it from session
        "user_id": request.form["user_id"]
    }
    if not Recipe.validate_recipe(data):
        return redirect("/new_recipe")

    # save the new recipe to the db
    Recipe.create_recipe(data)

    # redirect
    return redirect('/dashboard')

# =======================================
# Render Show One Recipe
# =======================================


@app.route('/recipe/<int:recipe_id>')
def show_recipe(recipe_id):
    if "user_id" not in session:
        flash("You have to login or register before entering =( sorry bout that...")
        return redirect("/")

    # query for recipe info with user info linked to it
    data = {
        "recipe_id" : recipe_id
    }

    recipe = Recipe.get_recipe_with_user(data)
    # send info to render the page with it

    return render_template("show_recipe.html", recipe=recipe)

# =======================================
# Render Edit Recipe Route
# =======================================

@app.route('/recipe/edit/<int:recipe_id>')
def edit_recipe(recipe_id):

    # query for recipe we want to update
    data = {
        "recipe_id" : recipe_id
    }

    recipe = Recipe.get_recipe_with_user(data)

    return render_template("edit_recipe.html", recipe=recipe)

# =======================================
# Process Edit Recipe Route
# =======================================

@app.route('/recipe/edit/<int:recipe_id>/process', methods=['POST'])
def edit_recipe_process(recipe_id):

    # validate, update, and then redirect

    if 'under_30' not in request.form:
        session['under_30'] = None
    else:
        session['under_30'] = request.form['under_30']

    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "under_30": session["under_30"],
        "instructions": request.form["instructions"],
        "recipe_id" : recipe_id #this is coming from the url
    }

    if not Recipe.validate_recipe(data):
        return redirect(f"/recipe/edit/{recipe_id}")

    Recipe.update_recipe(data)

    return redirect('/dashboard')

# =======================================
# Process Delete Recipe Route
# =======================================

@app.route('/recipe/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    
    data = {
        "recipe_id" : recipe_id
    }

    Recipe.delete_recipe(data)

    return redirect('/dashboard')