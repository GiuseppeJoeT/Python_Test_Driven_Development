import unittest
from vending_machine import give_change

# from where we import it?

# We define a class which inherits from unittest.TestCase
# This is necessary for the Python test runner to actually
# find our tests.

# A class can be thought of as a collection of tests,
# perhaps with similar functionality.


class TestVendingMachine(unittest.TestCase):

    def give_change(nAmount):
        return


    def test_return_change(self):
        self.assertEqual(give_change(17), [10, 5, 2], 'wrong change given')
        self.assertEqual(give_change(18), [10, 5, 2, 1], 'wrong change given')
        return


        # coins = self.give_change(17)
        # self.assertEqual(coins[10, 5, 2], 'wrong change given')
        # Because we inherited from unittest.TestCase, we have some
        # useful methods that we can use, such as assertEqual(), assertTrue(),
        # assertFalse().

        # The first two parameters are the two values which we want
        # to assert as equal (coins [10, 5, 2]); the last parameter is an optional message
        # which will be displayed if the test fails.
