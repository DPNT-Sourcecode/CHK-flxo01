from unittest import TestCase
from lib.solutions.CHK import checkout_solution


class TestCheckout(TestCase):
    def test_checkout(self):
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('ABCDF') == -1