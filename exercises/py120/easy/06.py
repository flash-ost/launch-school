"""
Pet Shelter
Consider the following code:

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
Write the classes and methods that will be necessary to make this code run, and log the following output:

P Hanson has adopted the following pets:
a cat named Cocoa
a cat named Cheddar
a bearded dragon named Darwin

B Holmes has adopted the following pets:
a dog named Molly
a parakeet named Sweetie Pie
a dog named Kennedy
a fish named Chester

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.
The order of the output does not matter, so long as all of the information is presented.

Further Exploration
Suppose the shelter has a number of not-yet-adopted pets, and wants to manage them through this same system. Thus, you should be able to add the following output to the example output shown above:
The Animal Shelter has the following unadopted pets:
a dog named Asta
a dog named Laddie
a cat named Fluffy
a cat named Kat
a cat named Ben
a parakeet named Chatterbox
a parakeet named Bluebell
   ...

P Hanson has 3 adopted pets.
B Holmes has 4 adopted pets.
The Animal shelter has 7 unadopted pets.
"""

class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name

    @property
    def species(self):
        return self._species

    @property
    def name(self):
        return self._name
    
    def info(self):
        print(f'a {self.species} named {self.name}')

class Owner:
    def __init__(self, name):
        self._name = name
        self._number_of_pets = 0

    @property
    def name(self):
        return self._name

    def number_of_pets(self):
        return self._number_of_pets

class Shelter:
    def __init__(self):
        self._adoptions = {}
        self._unadopted = []

    @property
    def adoptions(self):
        return self._adoptions
    
    @property
    def unadopted(self):
        return self._unadopted 
    
    def adopt(self, owner, pet):
        owner._number_of_pets += 1 
        self.adoptions[owner] = self.adoptions.get(owner, []) + [pet]

    def print_adoptions(self):
        for owner in self.adoptions:
            print(f'{owner.name} has adopted the following pets:')
            for pet in self.adoptions[owner]:
                pet.info()
            print()

    def print_unadopted(self):
        print('The Animal Shelter has the following unadopted pets:')
        for pet in self.unadopted:
            pet.info()
        print()   

    def add_pet(self, pet):
        self._unadopted += [pet]

    def number_of_pets(self):
        return len(self._unadopted)    

cocoa      = Pet('cat', 'Cocoa')
cheddar    = Pet('cat', 'Cheddar')
darwin     = Pet('bearded dragon', 'Darwin')
kennedy    = Pet('dog', 'Kennedy')
sweetie    = Pet('parakeet', 'Sweetie Pie')
molly      = Pet('dog', 'Molly')
chester    = Pet('fish', 'Chester')
asta       = Pet('dog', 'Asta')
laddie     = Pet('dog', 'Laddie')
fluffy     = Pet('cat', 'Fluffy')
kat        = Pet('cat', 'Kat')
ben        = Pet('cat', 'Ben')
chatterbox = Pet('parakeet', 'Chatterbox')
bluebell   = Pet('parakeet', 'Bluebell')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)
shelter.add_pet(asta)
shelter.add_pet(laddie)
shelter.add_pet(fluffy)
shelter.add_pet(kat)
shelter.add_pet(ben)
shelter.add_pet(chatterbox)
shelter.add_pet(bluebell)

shelter.print_adoptions()
shelter.print_unadopted()
print(f'{phanson.name} has {phanson.number_of_pets()} '
      "adopted pets.")
print(f'{bholmes.name} has {bholmes.number_of_pets()} '
      'adopted pets.')
print(f'The Animal shelter has {shelter.number_of_pets()} unadopted pets.')

