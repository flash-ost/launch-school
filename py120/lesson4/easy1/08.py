"""
Question 8
Suppose you have an object named my_obj and that you want to call a method named foo using my_obj as the caller. How can you see where Python will look for the method. You don't need to determine the actual method location; just identifying the search sequence is sufficient.
"""
# By accessing __mro__ (method resolution order) attribute of the class
# or calling its mro() method
class Dummy:
    def foo(self):
        pass

my_obj = Dummy()
print(my_obj.__class__.__mro__)
print(my_obj.__class__.mro())

