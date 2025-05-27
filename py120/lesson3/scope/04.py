class Dog:
    def __init__(self, breed):
        self._breed = breed

    @property
    def breed(self):
        return self._breed
    
doggo = Dog('Shiba')
doggo._breed = 'Husky'
print(doggo.breed)    