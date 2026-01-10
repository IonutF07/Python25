class Inhabitant:
    MAX_ENERGY = 100

    def __init__(self, name:"Inhabitant", age=0):
        self.name = name
        self.age = age
        self.energy = Inhabitant.MAX_ENERGY

    # Instance method: increase age by 1
    def grow(self):
        self.age += 1

    # Instance method: increase energy with max cap, return overflow if any
    def eat(self, amount):
        potential_energy = self.energy + amount
        if potential_energy > Inhabitant.MAX_ENERGY:
            self.energy = Inhabitant.MAX_ENERGY
            return potential_energy - self.energy
        else:
            self.energy = potential_energy
            return 0

    # Instance method: decrease energy with floor at 0, return shortfall if any
    def move(self, distance):
        potential_energy = self.energy - distance
        if potential_energy < 0:
            self.energy = 0
            return self.energy - abs(potential_energy)
        else:
            self.energy = potential_energy
            return 0