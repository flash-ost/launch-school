"""
Question 5
Modify the code from the previous question so that calling Hello.hi() on the class (rather than an instance) still uses Greeting's instance method greet() to print "Hi".
"""

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet('Hi')  

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

Hello.hi()        

        