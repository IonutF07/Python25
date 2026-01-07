# A simple Robot class demonstrating class attributes, instance attributes,
# static methods, and instance methods.
class Robot:
    # class attribute
    laws = "Protect, Obey and Survive"
    # class (constant) attribute
    MAX_ENERGY = 100

    # A static method
    @staticmethod
    def the_laws():
        print(Robot.laws)

    # An constructor method (special instance method)
    def __init__(self, name="Robot", age=0):
        # An instance attribute
        self.name = name
        self.age = age
        self.energy = Robot.MAX_ENERGY

    # An instance method
    def display(self):
        print(f"I am {self.name}")

    # Magic method for debugging / developer convenience
    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age}, energy={self.energy})"

    # Magic method for user-friendly output
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

# Testing the Robot class
if __name__ == "__main__":
    robot = Robot()
    print(repr(robot))
    print(robot)