"""
Define a Dog class that has a breed instance variable. Instantiate two objects from this class, one with the breed 'Golden Retriever' and another with the breed 'Poodle'. Print the breed of each dog.
"""
class Dog:
    def __init__(self, breed):
        self._breed = breed

    @property
    def breed(self):
        return self._breed    

gretriever = Dog('Golden Retriver')
poodle = Dog('Poodle')

print(gretriever.breed)
print(poodle.breed) 