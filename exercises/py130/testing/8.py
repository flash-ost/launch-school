"""
Same Object Assertions
Write a test that will fail if lst and the return value of lst.process are different objects.
"""

import unittest

class TestSameObject(unittest.TestCase):
    def setUp(self):
        self.lst = []

    def test_same_object(self):
        self.assertIs(self.lst, self.lst.process())

if __name__ == '__main__':
    unittest.main()        