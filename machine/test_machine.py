"""This class runs integrational test cases for testing CoffeeMachine"""

from __future__ import absolute_import

import logging
import unittest

import machine.machine_lib as ml

logger = logging.getLogger(__name__)


class TestMachine(unittest.TestCase):

    def test_integration(self):
        """
        This will load input from specified json file,fetching
        Coffee Machine details: outlets,ingredients, and list of
        beverages
        Create a coffee machine with these details
        Generate all possible outputs(combinations,quantity and ingredients left)
        for any successful permutation of beverages, for this machine
        Run the coffee machine to serve input beverages, sufficient times to
        generate all possible outputs, and verify the output
        Refill the machine after each serve
        """

        machine, beverages = ml.load_json('payload\input1.json')

        initial_ingredients = dict()
        for i in machine.ingredients:
            initial_ingredients[i.name] = i.quantity

        logger.info("available ingredients: %s", initial_ingredients)
        # all possible outputs
        completed_beverages_list, left_ingredients_dict = ml.get_outputs(
            machine, beverages)
        possible_outputs = len(completed_beverages_list)

        for i in range(2*possible_outputs):
            results, left_ingredients = machine.serve_beverages(beverages)
            completed = []
            logger.info("#%s status:", i)
            for result in results:
                is_completed, beverage_name, status = result
                logger.info(status)
                if is_completed:
                    completed.append(beverage_name)

            completed.sort()
            logger.info("left ingredients: %s", left_ingredients)

            # Asserting if completed beverages and left ingredients matches any output
            self.assertIn(completed, completed_beverages_list)
            self.assertEqual(left_ingredients,
                             left_ingredients_dict[tuple(completed)])

            machine.refill()
