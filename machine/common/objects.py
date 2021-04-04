""" Beverage and Ingredient classes """


class Beverage:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f'{self.name}'


class Ingredient:
    def __init__(self, ingredient_name, ingredient_quantity):
        self.name = ingredient_name
        self.quantity = ingredient_quantity

    def __str__(self):
        return f'{self.name} : {self.quantity}'
