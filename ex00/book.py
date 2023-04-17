from datetime import datetime
from typing import Dict
from recipe import Recipe

class Book:
    name: str
    last_update: datetime
    creation_date: datetime
    recipes_list: Dict[str, list]

    def __init__(self, name: str):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_list in self.recipes_list.values():
            for recipe in recipe_list:
                if name == recipe.name:
                    print(recipe)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        for recipe in self.recipes_list[recipe_type]:
            txt = str(recipe)
            print(txt)


    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
        print("Recipe added succesfully")
