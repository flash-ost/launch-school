"""
Equality Assertions
Write a unittest assertion that will fail if value.lower does not return 'xyz'.
"""

import unittest

class TestEquality(unittest.TestCase):
    def setUp(self):
        self.value = 'ABC'

    def test_equality(self):
        self.assertEqual('xyz', self.value.lower())

if __name__ == '__main__':
    unittest.main()        