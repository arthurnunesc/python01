from typing import List
from enum import Enum


class RecipeType(Enum):
    STARTER = "starter"
    LUNCH = "lunch"
    DESSERT = "dessert"


class Recipe:
    def __init__(
        self,
        name: str,
        cooking_lvl: int,
        cooking_time: int,
        ingredients: List[str],
        recipe_type: RecipeType,
        description: str or None,
    ):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"""Recipe name: {self.name.capitalize()}
Cooking Level: {self.cooking_lvl}
Cooking Time: {self.cooking_time}
Description: {self.description}
Recipe Type: {self.recipe_type.capitalize()}\n"""
        return txt
