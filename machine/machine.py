from __future__ import absolute_import

from machine.machine_db import MachineDB
import multiprocessing as mp


class Machine:

    def __init__(self, outlets, ingredients):
        self.outlets = outlets
        self.ingredients = ingredients
        self.db = MachineDB()
        self.add_ingredients(ingredients)

    def add_ingredients(self, ingredients):
        self.db.add_ingredients(ingredients)

    def refill(self):
        self.db.update_ingredients(self.ingredients)

    def serve(self, beverage):
        available_ingredients = dict()
        for ingredient in beverage.ingredients:
            available_quantity = self.db.get_ingredient_quantity(
                ingredient.name)
            if not available_quantity:
                status = f'{beverage.name} cannot be prepared because {ingredient.name} is not avaialble'
                return False, beverage.name, status

            desired_quantity = ingredient.quantity
            if desired_quantity > available_quantity:
                status = f'{beverage.name} cannot be prepared because {ingredient.name} is not sufficient'
                return False, beverage.name, status

            available_ingredients[ingredient.name] = desired_quantity

        is_completed, beverage_name, status = self.db.update_ingredients_decrement(
            available_ingredients, beverage.name)
        return is_completed, beverage_name, status

    def serve_beverages(self, beverages):

        # create a pool of with no. of parallel processes as outlets
        count = min(self.outlets, mp.cpu_count())

        with mp.Pool(processes=count) as p:
            results = p.map(self.serve, beverages)
            left_ingredients = dict()
            for i in self.db.get_all_ingredients():
                left_ingredients[i.name] = i.quantity
            return results, left_ingredients
