from unittest import TestCase
from lib.solutions.HLO import hello_solution


class TestHello(TestCase):
    def test_raises_error(self):
        with self.assertRaises(TypeError):
            hello_solution.hello(1)

    def test_returns_message(self):
        assert hello_solution.hello('world') == 'hello'
