class Animal:
    def __init__(self, name: str, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

class Plant:
    def __init__(self, name: str, edible: bool = False):
        self.name = name
        self.edible = edible
        
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    pass