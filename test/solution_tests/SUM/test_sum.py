from lib.solutions.SUM import sum_solution
from unittest import TestCase


class TestSum(TestCase):
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(0, 100) == 100

    def test_raise_error_if_less_than_zero(self):
        with self.assertRaises(ValueError):
            sum_solution.compute(-1, 2)

    def test_raise_error_if_more_than_one_hundred(self):
        with self.assertRaises(ValueError):
            sum_solution.compute(0, 101)

    def test_raise_error_if_not_integer(self):
        with self.assertRaises(ValueError):
            sum_solution.compute(0.5, 10)



