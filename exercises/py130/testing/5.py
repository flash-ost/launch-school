"""
Not Included Object Assertions
Write a test that will fail if 'xyz' is one of the elements in the list lst:
"""

import unittest

class TestNotIncludedObject(unittest.TestCase):
    def setUp(self):
        self.lst = ['xyz']

    def test_not_included_object(self):
        self.assertNotIn('xyz', self.lst)

if __name__ == '__main__':
    unittest.main()            