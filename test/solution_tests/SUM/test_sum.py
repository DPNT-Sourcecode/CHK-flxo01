from lib.solutions.SUM import sum_solution
from unittest import TestCase


class TestSum(TestCase):
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_raise_error_if_less_than_zero(self):
        with ValueError:
            sum_solution.compute(-1, 2)


