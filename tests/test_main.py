import unittest
from main import simple_count, complex_function
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    def test_simple_function1(self):
        self.assertEqual(0, simple_count(''))

    def test_simple_function2(self):
        self.assertEqual(5, simple_count('hello'))

    def test_complex_function(self):
        self.assertEqual('behaviour 1', complex_function())

    @patch('main.random_function')
    def test_complex_function_with_mock(self, mock_random_function):
        mock_random_function.return_value = True
        self.assertEqual('behaviour 1', complex_function())
        
