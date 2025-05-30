"""
Question 4
Suppose we have this code:

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')
Without running the above code, what would each snippet do were you to run it?

Snippet 1
hello = Hello()
hello.hi()
Snippet 2
hello = Hello()
hello.bye()
Snippet 3
hello = Hello()
hello.greet()
Snippet 4
hello = Hello()
hello.greet('Goodbye')
Snippet 5
Hello.hi()
"""
class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

# Snippet 1
hello = Hello()
hello.hi() # Hello

# Snippet 2
hello = Hello()
hello.bye() # AttributeError: Hello instance has no attribute 'bye'

# Snippet 3
hello = Hello()
hello.greet() # TypeError: greet() takes 2 positional arguments (1 given)

# Snippet 4
hello = Hello()
hello.greet('Goodbye') # Goodbye

# Snippet 5
Hello.hi() # TypeError: missing required positional argument self (we didn't create instance)