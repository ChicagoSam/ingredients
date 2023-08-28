#Importing Resources
import requests

#Defining Variables
#to do: mask APP ID and KEY
API_URL = "https://api.edamam.com/api/recipes/v2?type=public"
APP_ID = "32aabb7c"
APP_KEY = "2d280e0b89edb69ca1ca6fdf9f0d145a"

def get_matching_recipes(ingredients):
    #1st option formats ingredients as (x,y,z) vs 2nd (x, y, z) -- API changing it up
    url = f"{API_URL}&q={'%2C'.join(ingredients)}&app_id={APP_ID}&app_key={APP_KEY}"
    print(url)
    response = requests.get(url)

    #response = requests.get(f"{API_URL}&q={'%2C%20'.join(ingredients)}&app_id={APP_ID}&app_key={APP_KEY}")

    if response.status_code == 200: #Ensuring API call was successful
        recipe_list = response.json()
        ## BELOW LINE PERHAPS TROUBLE? ##
        ## List: hits, dictionary: recipe, dictionary: label / source / url ##
        matching_recipes = recipe_list.get("hits", []) #Extracts list of recipes
    
        for hit in matching_recipes:
            recipe_name = hit['recipe']['label']
            recipe_url = hit['recipe']['url']
            recipe_ingredients = hit['recipe']['ingredients']
            recipeDict = {}
            recipeDict['name'] = recipe_name
            recipeDict['url'] = recipe_url
            recipeDict['ingredients'] = recipe_ingredients
            matching_recipes.append(recipeDict)
        
        return matching_recipes
            

    else:
        error_message = "API call failed. Please try again later."
        return error_message
