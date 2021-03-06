"""
Recipie Interpreter
"""
import json
import mealmaker_constants as MMK

class RecipieReader(object):
    "Recipie Interpreter Class"

    def __init__(self, recipie_file):
        """
        Init function for RecipieReader Class

        :param str recipie_file: absolute path to recipie json file
        :raises IOError: if recipie_file not found
        :raises ValueError: if error opening recipie_file
        :raises KeyError: if necessary keys are missing from recipie_file
        """
        try:
            with open(recipie_file) as json_file:
                self.recipie = json.load(json_file)
        except IOError as io_error:
            raise IOError('File not found: {}'.format(io_error.filename))

        try:
            self.ing_pop = self.recipie[MMK.KEY_ING_PROP]
            self.steps = self.recipie[MMK.KEY_STEPS]
            self.pan = self.recipie[MMK.KEY_PAN]
        except KeyError as key_err:
            raise KeyError('{} not found in recipie'
                           .format(key_err))

    def get_ingredient_props(self):
        """
        Return dict of properties of ingredients of the RecipieReader instance

        :return dict self.ingredients: dict of properties of ingredients
        """
        return self.ing_pop

    def get_steps(self):
        """
        Return dict of steps of the RecipieReader instance

        :return dict self.steps: dict of steps
        """
        return self.steps

    def get_pans(self):
        """
        Return pan(s) of the RecipieReader instance

        :return int self.pan: Pan number
        """
        return self.pan

    def validate_recipie(self):
        """
        # TODO: Write function to validate recipie
        # Make sure all ingredients in the steps have dispensers defined
        # in ing_prop
        """
        return 0
