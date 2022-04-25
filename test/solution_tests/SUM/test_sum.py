from lib.solutions.SUM import sum_solution
from unittest import TestCase


class TestSum(TestCase):
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

