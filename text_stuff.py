import unittest


class TestThatStuffWorks(unittest.TestCase):
    def test_this_thing_is_on(self):
        self.assertNotEqual(1, 1)

#class TestVendingMachine(unittest.TestCase):
#    def give_change = (self, amount):
#        if amount == 0:

#        return [10, 5, 2]

    def test_return_change(self):
        coins = self.give_change(17)
        self.assertEqual(coins, [10, 5, 2])