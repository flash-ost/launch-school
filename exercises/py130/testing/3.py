"""
None Assertions
Write a unittest assertion that will fail if value is not None.
"""

import unittest

class TestNone(unittest.TestCase):
    def setUp(self):
        self.value = 'None'
    
    def test_none(self):
        self.assertIsNone(self.value)

if __name__ == '__main__':
    unittest.main()        