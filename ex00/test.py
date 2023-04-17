from book import Book
from recipe import Recipe


def main():
    my_book = Book("THE BOOK")
    my2_book = Book("THE BOOK 2")
    sandwich_obj = Recipe(
        "sandwich",
        2,
        5,
        ["ham", "bread", "cheese", "tomatoes"],
        "lunch",
        "LOL GOOD SANDWICH",
    )
    cake_obj = Recipe(
        "cake", 10, 45, ["flour", "sugar", "eggs"], "dessert", "LOL GOOD CAKE"
    )
    salad_obj = Recipe(
        "salad",
        4,
        25,
        ["avocado", "arugula", "tomatoes", "spinach"],
        "lunch",
        "LOL GOOD SALAD",
    )
    
    my_book.add_recipe(sandwich_obj)
    my2_book.add_recipe(cake_obj)
    my2_book.add_recipe(salad_obj)
    my_book.get_recipe_by_name("sandwich")
    my_book.get_recipes_by_types("lunch")


if __name__ == "__main__":
    main()
