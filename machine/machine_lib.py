"""Helper functions for processing input json for coffee-machine"""

from __future__ import absolute_import

import json
from itertools import permutations

from machine.common.objects import Beverage, Ingredient
from machine.machine import Machine


def load_json(file_name):
    """
    Convert json into Machine, Beverages Objects
    """
    with open(file_name, "r") as f:
        data = json.loads(f.read())
        machine = data["machine"]
        outlets = machine["outlets"]["count_n"]

        ingredients = list()
        for (i, v) in machine["total_items_quantity"].items():
            ingredients.append(Ingredient(
                ingredient_name=i, ingredient_quantity=v))

        coffee_machine = Machine(outlets=outlets, ingredients=ingredients)

    beverages = list()
    for (i, v) in machine["beverages"].items():
        beverages.append(Beverage(name=i, ingredients=[
                         Ingredient(name, v[name]) for name in v]))

    return coffee_machine, beverages


def get_outputs(machine, beverages):
    """
    Generate all possible outputs for (Machine, Beverages)
    Returns:
    1) completed_beverages: [["hot_tea","hot_coffee"], ..]
    2) left_ingredients:
    {("hot_tea","hot_coffee"):{"hot_water": 100,"hot_milk": 0,"ginger_syrup": 100,}...}
    """

    completed_beverages = []
    left_ingredients = dict()
    perm = permutations(beverages)
    for seq in list(perm):
        completed = []
        available = get_ingredients(machine)
        for bev in seq:
            if is_beverage_possible(bev, available):
                serve_beverage(bev, available)
                completed.append(bev.name)
        completed.sort()
        if completed not in completed_beverages:
            completed_beverages.append(completed)
            left_ingredients[tuple(completed)] = available

    return completed_beverages, left_ingredients


def get_ingredients(machine):

    res = dict()
    for ingredient in machine.ingredients:
        res[ingredient.name] = ingredient.quantity
    return res


def is_beverage_possible(beverage, ingredients):

    for i in beverage.ingredients:
        rq = i.quantity
        if i.name not in ingredients:
            return False
        aq = ingredients[i.name]
        if rq > aq:
            return False
    return True


def serve_beverage(beverage, ingredients):

    for i in beverage.ingredients:
        rq = i.quantity
        aq = ingredients[i.name]
        ingredients[i.name] = aq-rq
