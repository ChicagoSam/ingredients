#!/usr/bin/env python3
from flask import Flask, render_template, request
from utils import get_matching_recipes

app = Flask (__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients').split(',')
        recipes = get_matching_recipes(ingredients)
        # recipes = the value of "hits" from the API; a list of dictionaries, every dictionary being a different recipe
        return render_template('index.html', recipes=recipes, ingredients=ingredients)
    #If GET, show blank page
    return render_template('index.html', recipes=None, ingredients=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225, debug=True)
