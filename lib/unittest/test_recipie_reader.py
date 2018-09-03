"""Unit test module for recipie_reader.py"""
import unittest
import os
import sys
import json

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SRC_DIR + "/..")
import recipie_reader
import mealmaker_constants as MMK

T_JSON_RECIPIE_FILENAME = os.path.join(SRC_DIR, '../recipies/salt_water.json')
T_JSON_RECIPIE_STR = open(T_JSON_RECIPIE_FILENAME).read()
T_JSON_RECIPIE = json.loads(T_JSON_RECIPIE_STR)

class TestRecipieReader(unittest.TestCase):
    """Unit Test Class"""

    def setUp(self):
        """setup before each test"""

    def test_init_success(self):
        """Test the __init__ function for success"""
        self.recipie_reader = recipie_reader.RecipieReader(T_JSON_RECIPIE_FILENAME)
        # Validate necessary keys in recipie
        for key in MMK.KEY_INGREDIENTS, MMK.KEY_INSTRUCTIONS, MMK.KEY_PAN:
            self.assertIn(key, self.recipie_reader.recipie)
        # Validate ingredients
        for key in MMK.ING_SALT, MMK.ING_WATER:
            self.assertIn(key, self.recipie_reader.recipie[MMK.KEY_INGREDIENTS])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRecipieReader)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
