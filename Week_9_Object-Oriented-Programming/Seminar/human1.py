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

# Testing the Human class
if __name__ == "__main__":
    human = Human()
    print(repr(human))
    print(human)