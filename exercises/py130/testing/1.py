"""
Boolean Assertions
Write a unittest assertion that will fail if value % 2 != 0 is not True.
"""
import unittest

class TestBoolean(unittest.TestCase):
    def setUp(self):
        self.value = 4

    def test_boolean(self):
        self.assertTrue(self.value % 2 != 0, 'value is not odd')

if __name__ == '__main__':
    unittest.main()        