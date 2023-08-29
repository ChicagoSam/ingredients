import requests
import pytest
from utils import get_matching_recipes
import routes

#a url which returns json data for recipes with lemon, sugar, and water as ingredients
lsw_url = "https://api.edamam.com/api/recipes/v2?type=public&q=lemon%2Csugar%2Cwater&app_id=32aabb7c&app_key=2d280e0b89edb69ca1ca6fdf9f0d145a"

#ensure utils returns the correct list
def test_get_matching_recipes():
    assert get_matching_recipes('lemon,sugar,water') == requests.get(lsw_url).json().get('hits')
