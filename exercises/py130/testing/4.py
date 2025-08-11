"""
Included Object Assertions
Write a unittest assertion that will fail if the 'xyz' is not in the list lst.
"""

import unittest

class TestIncludedObject(unittest.TestCase):
    def setUp(self):
        self.lst = ['abc']

    def test_included_object(self):
        self.assertIn('xyz', self.lst)

if __name__ == '__main__':
    unittest.main()