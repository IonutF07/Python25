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

# Testing the Robot class
if __name__ == "__main__":
    robot = Robot()
    robot.display()
    Robot.the_laws()