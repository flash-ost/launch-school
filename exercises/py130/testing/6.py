"""
Exception Assertions
Write a unittest assertion that will fail unless employee.hire raises a NoExperienceError exception.
"""

import unittest

class NoExperienceError(Exception):
    def __init__(self, message='Employee doesn\'n have necessary experience'):
        super().__init__(message)

class Employee:
    def __init__(self):
        self.experience = None

    def hire(self):
        if self.experience is None:
            raise NoExperienceError

class TestException(unittest.TestCase):
    def setUp(self):
        self.employee = Employee()

    def test_exception(self):
        with self.assertRaises(NoExperienceError):
            self.employee.hire()

if __name__ == '__main__':
    unittest.main()            