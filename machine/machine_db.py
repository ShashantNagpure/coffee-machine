from __future__ import absolute_import

from machine.common.objects import Ingredient
import apsw


class MachineDB:

    def __init__(self):
        cursor = self.get_connection()
        cursor.execute("DROP TABLE IF EXISTS ingredients")
        cursor.execute(
            "CREATE TABLE ingredients(name TEXT, value INT CHECK(value >= 0))")

    def add_ingredients(self, ingredients):
        cursor = self.get_connection()
        for ingredient in ingredients:
            cursor.execute("insert INTO ingredients values(?,?)",
                           (ingredient.name, ingredient.quantity,))

    def get_ingredient_quantity(self, ingredient_name):

        cursor = self.get_connection()
        cursor.execute(
            'SELECT value FROM ingredients where "name" = ?', (ingredient_name,))
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def get_all_ingredients(self):

        cursor = self.get_connection()
        cursor.execute("SELECT * from ingredients")
        rows = cursor.fetchall()
        ingredients = list()
        for row in rows:
            ingredients.append(Ingredient(
                ingredient_name=row[0], ingredient_quantity=row[1]))
        return ingredients

    def update_ingredients_decrement(self, ingredients, beverage):
        """
        transaction with rollback option if any decrement fails due to value>=0 constraint
        """

        cursor = self.get_connection()
        cursor.execute("BEGIN IMMEDIATE")
        for ingredient in ingredients:
            try:
                cursor.execute('UPDATE ingredients SET value = value - ? where "name" = ?',
                               (ingredients[ingredient], ingredient))
            except apsw.ConstraintError:
                cursor.execute('ROLLBACK')
                return False, beverage, f'{beverage} cannot be prepared because {ingredient} is not sufficient'

        cursor.execute('COMMIT')

        return True, beverage, f'{beverage} is prepared'

    def update_ingredients(self, ingredients):
        cursor = self.get_connection()
        for i in ingredients:
            cursor.execute(
                'UPDATE ingredients SET value = ? where "name" = ?', (i.quantity, i.name))

    @staticmethod
    def get_connection():
        con = apsw.Connection('coffee.db')
        con.setbusytimeout(500)
        con.cursor().execute('pragma journal_mode=wal')
        return con.cursor()
