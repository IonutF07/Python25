# Simple Human class with attributes and methods
class Human:
    # class (constant) attribute
    MAX_ENERGY = 100

    # constructor method
    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    # method to display human details
    def display(self):
        print(f"I am {self.name}")

    # Magic method for debugging / developer convenience
    def __repr__(self):
        return f"human(name={self.name}, age={self.age}, energy={self.energy})"

    # Magic method for user-friendly output
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

# Instance method: increase energy with max cap, return overflow if any
    def eat(self, amount):
        potential_energy = self.energy + amount
        if potential_energy > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
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

if __name__ == "__main__":
    human = Human()
    print(repr(human))
    human.move(10)
    print(repr(human))
    human.eat(5)
    print(repr(human))