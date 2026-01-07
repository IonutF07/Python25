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

# Testing the Human class
if __name__ == "__main__":
    human = Human()
    human.display()