from unittest import TestCase
from lib.solutions.CHK import checkout_solution


class TestCheckout(TestCase):
    def test_checkout(self):
        # assert checkout_solution.checkout('ABCD') == 115
        # assert checkout_solution.checkout('ABCDW') == -1
        # assert checkout_solution.checkout('123') == -1
        # assert checkout_solution.checkout('abcd') == -1
        # assert checkout_solution.checkout('AAA') == 130
        # assert checkout_solution.checkout('AAAA') == 130 + 50
        # assert checkout_solution.checkout('AAAAA') == 200
        # assert checkout_solution.checkout('AAAAAAAAA') == 200 + 130 + 50
        # assert checkout_solution.checkout('BB') == 45
        # assert checkout_solution.checkout('BBB') == 45 + 30
        # assert checkout_solution.checkout('CC') == 40
        # assert checkout_solution.checkout('DD') == 30
        # assert checkout_solution.checkout('ABCDABA') == 175 + 35
        # assert checkout_solution.checkout('E') == 40
        # assert checkout_solution.checkout('EEB') == 80
        # assert checkout_solution.checkout('EE') == 80
        # assert checkout_solution.checkout('EEBB') == 80 + 30
        # assert checkout_solution.checkout('EEEB') == 120
        # assert checkout_solution.checkout('EEBBB') == 80 + 45
        # 
        # assert checkout_solution.checkout('F') == 10
        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('FFF') == 20


