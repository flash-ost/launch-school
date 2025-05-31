"""
CoursesPY120 Object-Oriented Programming with PythonOO Practice Problems4. Practice Problems: Medium 1
Give us your feedback
Practice Problems: Medium 1
Question 1
Alyssa asked Ben to code review the following code:

class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance
Ben glanced over the code quickly and said - "It looks fine, except that you're trying to access self.balance instead of self._balance in the balance_is_positive method."

"Not so fast," Alyssa replied. "What I'm doing here is valid; I can definitely use self.balance there!"

Who is correct, Ben or Alyssa? Why?
"""
# Alyssa is right. Inside balance_is_positive she uses a getter property
class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance
    
acc = BankAccount(500)
print(acc.balance_is_positive())    
    