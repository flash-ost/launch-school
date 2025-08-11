"""
Type Assertions
Write a unittest assertion that will fail if value is not an instance of the Numeric class exactly. value should not be an instance of one of Numeric's superclasses.
"""

import unittest

class Numeric:
    pass

class TestType(unittest.TestCase):
    def setUp(self):
        self.value = True

    def test_type(self):
        self.assertIsInstance(self.value, Numeric)

if __name__ == '__main__':
    unittest.main()        