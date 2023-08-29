#!/usr/bin/env python3
"""Recipe Final Project | Benji Osborn, Demetra Hill, Sammy Tamimi"""


from flask import Flask, render_template, request
from utils import get_matching_recipes

app = Flask (__name__)

# Route for handling both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve ingredients from form input and split into a list
        ingredients = request.form.get('ingredients').split(',')
        # Get recipes that match the provided ingredients
        # recipes = the value of "hits" from the API; a list of dictionaries, every dictionary being a different recipe
        recipes = get_matching_recipes(ingredients)
        # Return the template with matching recipes and entered ingredients
        return render_template('index.html', recipes=recipes, ingredients=ingredients)
    #If GET, show blank page
    return render_template('index.html', recipes=None, ingredients=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225, debug=True)
