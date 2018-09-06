"""Unit test module for recipie_reader.py"""
import unittest
import os
import sys
import json
import mock

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SRC_DIR + "/..")
import recipie_reader  # pylint: disable=import-error
import mealmaker_constants as MMK  # pylint: disable=import-error

T_JSON_RECIPIE_FILENAME = os.path.join(SRC_DIR, '../recipies/salt_water.json')
T_JSON_RECIPIE_STR = open(T_JSON_RECIPIE_FILENAME).read()
T_JSON_RECIPIE = json.loads(T_JSON_RECIPIE_STR)


class TestRecipieReader(unittest.TestCase):
    """Unit Test Class"""

    def setUp(self):
        """setup before each test"""
        self.reader = recipie_reader.RecipieReader(T_JSON_RECIPIE_FILENAME)

    def test_init_success(self):
        """Test the __init__ function for success"""
        # Validate necessary keys in recipie
        for key in MMK.KEY_INGREDIENTS, MMK.KEY_STEPS, MMK.KEY_PAN:
            self.assertIn(key, self.reader.recipie)
        # Validate ingredients
        for key in MMK.ING_SALT, MMK.ING_WATER:
            self.assertIn(key, self.reader.recipie[MMK.KEY_INGREDIENTS])
        # Verify that at least one step exists
        self.assertIn("1", self.reader.recipie[MMK.KEY_STEPS])

    def test_init_no_recipie_file(self):
        """Test the __init__ function when no recipie_file found"""
        with self.assertRaises(IOError) as io_exc:
            recipie_reader.RecipieReader("")
        self.assertTrue('File not found' in str(io_exc.exception))

    @mock.patch('json.load')
    @mock.patch('__builtin__.open')
    def test_init_ker_error(self, mock_open, mock_json_load):
        """Test the __init__ function when recipie_file is missing keys"""
        mock_open.return_value = mock.MagicMock()
        mock_json_load.return_value = json.loads("""{}""")
        with self.assertRaises(KeyError) as key_err:
            recipie_reader.RecipieReader("")
        self.assertTrue("ingredients' not found in recipie" in str(key_err.exception))

    def test_get_ingredients(self):
        """Test get_ingredients"""
        for key in MMK.ING_SALT, MMK.ING_WATER:
            self.assertIn(key, self.reader.get_ingredients())

    def test_get_steps(self):
        """Test get_steps"""
        self.assertIn("1", self.reader.get_steps())

    def test_get_pan(self):
        """Test get_pan"""
        self.assertEquals(0, self.reader.get_pans())


if __name__ == '__main__':
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestRecipieReader)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
    unittest.main()
