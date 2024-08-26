import unittest
from cornflask import cornflakes


class Test_Biggest_odd(unittest.TestCase):

    def test_that_biggest_odd_function(self):
        cornflakes.biggest_odd ("23956")

    def test_biggest_function_returns_biggest_odd(self):
        result = cornflakes.biggest_odd("23956")
        self.assertEqual(result, 9)

    def test_that_function_takes_two_arguments(self, number2):
        cornflakes.equal_string(self, number2)