from unittest import TestCase
from lib.solutions.CHK import checkout_solution


class TestCheckout(TestCase):
    def test_checkout(self):
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('ABCD1') == -1
        assert checkout_solution.checkout('123') == -1
        assert checkout_solution.checkout('abcd') == -1
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 130 + 50
        assert checkout_solution.checkout('AAAAA') == 200
        assert checkout_solution.checkout('AAAAAAAAA') == 200 + 130 + 50
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('BBB') == 45 + 30
        assert checkout_solution.checkout('CC') == 40
        assert checkout_solution.checkout('DD') == 30
        assert checkout_solution.checkout('ABCDABA') == 175 + 35
        assert checkout_solution.checkout('E') == 40
        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('EE') == 80
        assert checkout_solution.checkout('EEBB') == 80 + 30
        assert checkout_solution.checkout('EEEB') == 120
        assert checkout_solution.checkout('EEBBB') == 80 + 45
        assert checkout_solution.checkout('F') == 10
        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('FFFF') == 20 + 10
        assert checkout_solution.checkout('FFFFF') == 20 + 20
        assert checkout_solution.checkout('FFFFFF') == 20 + 20

        assert checkout_solution.checkout('H') == 10
        assert checkout_solution.checkout('HH') == 20
        assert checkout_solution.checkout('HHHHH') == 45
        assert checkout_solution.checkout('HHHHHH') == 45 + 10

        assert checkout_solution.checkout('N') == 40
        assert checkout_solution.checkout('NN') == 80
        assert checkout_solution.checkout('NNN') == 120
        assert checkout_solution.checkout('NNNM') == 120
        assert checkout_solution.checkout('NNNMM') == 120 + 15

        assert checkout_solution.checkout('PPP') == 50 * 3
        assert checkout_solution.checkout('PPPPP') == 200

        assert checkout_solution.checkout('STX') == 45
        assert checkout_solution.checkout('STZ') == 45
        assert checkout_solution.checkout('STZX') == 45 + 17
        assert checkout_solution.checkout('STZXZZ') == 45 + 45
        assert checkout_solution.checkout('STZXZZY') == 45 + 45 + 17
        assert checkout_solution.checkout('STZXZZYT') == 45 + 45 + 17 + 20
        assert checkout_solution.checkout('SSSXT') == 45 + 17 + 20
        assert checkout_solution.checkout('STZRRR') == 45 + 150
        assert checkout_solution.checkout('STZRRRQ') == 45 + 150
        assert checkout_solution.checkout('STZRRRQAAA') == 45 + 150 + 130
        assert checkout_solution.checkout('STZRRRQAAAAA') == 45 + 150 + 200
        assert checkout_solution.checkout('STZRRRQAAAFF') == 45 + 150 + 130 + 20
        assert checkout_solution.checkout('STZRRRQAAAFFF') == 45 + 150 + 130 + 20


