"""
Reverse Engineering
Write a class such that the following code prints the results indicated by the comments:

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz
"""
class Transform:
    @classmethod
    def lowercase(cls, data):
        return data.lower()
    
    def __init__(self, data):
        self.data = data

    def uppercase(self):
        return self.data.upper()    

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz