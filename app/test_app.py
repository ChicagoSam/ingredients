import requests
import pytest
from utils import get_matching_recipes
import routes

lsw_url = "https://api.edamam.com/api/recipes/v2?type=public&q=lemon%2Csugar%2Cwater&app_id=32aabb7c&app_key=2d280e0b89edb69ca1ca6fdf9f0d145a"

#ensure utils returns the correct list
def test_get_matching_recipes():
    function_list = get_matching_recipes(['lemon', 'sugar', 'water'])
    url_list = requests.get(lsw_url).json().get('hits')
    for hit in range(20):
        assert function_list[hit]['recipe']['label'] == url_list[hit]['recipe']['label']

# ensure the server returns nothing when given nonsense ingredients
def test_not_matching_recipes():
    edge_cases = [['342139847219834012'], ['asdfkjnokdfkboekjrdnvoksjdlkfjalsjdf'], ['this_is_not_an_existing_ingredient']]
    for val in edge_cases:
        assert get_matching_recipes(val) == []

# test what happens if something other than a GET or POST is sent to your page
SERVER_URL = "http://10.14.192.38:2225"  # Replace with the actual URL of your server

def test_disallowed_methods(): 
    disallowed_methods = ["PATCH", "DELETE", "PUT"]

    for method in disallowed_methods:
        response = requests.request(method, SERVER_URL)
        assert response.status_code == 405, f"Expected 405 status code for {method} request"
