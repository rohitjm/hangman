import unittest
from main import *


class TestUserGuess(unittest.TestCase):

    def test_valid_guess(self):
        self.chosen_word = "APPLE"
        self.assertTrue(check_input("A", self.chosen_word))


    def test_invalid_guess(self):
        self.chosen_word = "APPLE"
        self.assertFalse(check_input("B", self.chosen_word))


if __name__ == "__main__":
    # If called like a script, run our tests
    unittest.main(verbosity=2)
