"""
Modify the Student class from your answer to the previous problem. The modified class should have an instance variable called name that gets initialized during instantiation. Create two Student objects with different names but the same school, then print the name and school for both students.
"""
class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

stud1 = Student('Howard')
stud2 = Student('Susan')

print(f'{stud1.name}, {stud1.__class__.school_name}')
print(f'{stud2.name}, {stud2.__class__.school_name}')