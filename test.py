import unittest
from main import add

class TestAdd(unittest.TestCase):

    def test_add_result(self):
        self.assertEqual(add(3, 5), 8)
