#Importing Resources
import requests

#Defining Variables
#to do: mask APP ID and KEY
API_URL = "https://api.edamam.com/api/recipes/v2?type=public"
APP_ID = "32aabb7c"
APP_KEY = "2d280e0b89edb69ca1ca6fdf9f0d145a"

def get_matching_recipes(ingredients):
    #if API wants a space
    #url = f"{API_URL}&q={'%2C%20'.join(ingredients)}&app_id={APP_ID}&app_key={APP_KEY}"

    url = f"{API_URL}&q={'%2C'.join(ingredients)}&app_id={APP_ID}&app_key={APP_KEY}"
    #print(url)
    response = requests.get(url)

    if response.status_code == 200: #Ensuring API call was successful
        recipe_list = response.json()
        matching_recipes = recipe_list.get("hits", []) #Extracts list of recipes
        return matching_recipes
    else:
        error_message = "API call failed. Please try again later."
        return error_message
