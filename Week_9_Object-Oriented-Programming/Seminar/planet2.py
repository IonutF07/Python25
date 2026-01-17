# Define the Planet class which can hold humans and robots
from human1 import Human
from robot1 import Robot

class Planet:

    def __init__(self, name):
        # Store planet name
        self.name = name

        # Store inhabitants in a dictionary (humans + robots)
        self.inhabitants = {
            'humans': [],
            'robots': []
        }

    def __repr__(self):# Developer-friendly representation
        return f"planet(humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"

    def __str__(self):# User-friendly representation
        return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots."

    def add_human(self, human):# Add a human object to the humans list
        self.inhabitants['humans'].append(human)

    def add_robot(self, robot):# Add a robot object to the robots list
        self.inhabitants['robots'].append(robot)

    def remove_human(self, human):# Remove a human object from the humans list
        self.inhabitants['humans'].remove(human)

    def remove_robot(self, robot):# Remove a robot object from the robots list
        self.inhabitants['robots'].remove(robot)

if (__name__ == "__main__"):
    planet = Planet("Earth")
    print(repr(planet))
    prins = Human("Prins")
    planet.add_human(prins)
    print(repr(planet))
    print(planet)