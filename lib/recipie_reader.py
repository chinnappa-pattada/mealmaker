"""
Recipie Interpreter
"""
import json
import mealmaker_constants as MMK


class RecipieReader():
    "Recipie Interpreter Class"

    def __init__(self, recipie_file):
        """
        :param str recipie_file: absolute path to recipie json file
        raises:
        """
        try:
            with open(recipie_file) as json_file:
                self.recipie = json.load(json_file)
        except IOError as io_error:
            raise IOError('File not found: {}'.format(io_error.filename))
        except:
            raise ValueError('Unexpected error opening {}'.format(recipie_file))

        try:
            self.ingredients = self.recipie[MMK.KEY_INGREDIENTS]
        except KeyError as key_error:
            raise KeyError('{} not found in recipie'.format(MMK.KEY_INGREDIENTS))



    def getIngredients(self):
        """
        Return dict of ingredients of the RecipieReader instance
        :param str
        """
        return 0

    def getSteps(self):
        """
        Return
        """
        return 0
