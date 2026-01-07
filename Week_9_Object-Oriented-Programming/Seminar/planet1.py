# Define the Planet class that can hold Human and Robot objects
from human1 import Human
from robot1 import Robot

class Planet:

    def __init__(self, name):
        # Planet name
        self.name = name
        # Lists of inhabitants
        self.humans = []
        self.robots = []

    # Add a Human object to the planet
    def add_human(self, human):
        self.humans.append(human)

    # Remove a Human object from the planet
    def remove_human(self, human):
        if human in self.humans:
            self.humans.remove(human)

    # Add a Robot object to the planet
    def add_robot(self, robot):
        self.robots.append(robot)

    # Remove a Robot object from the planet
    def remove_robot(self, robot):
        if robot in self.robots:
            self.robots.remove(robot)

# Testing the Planet class
if __name__ == "__main__":
    planet = Planet("Earth")

    # Create objects
    human = Human()
    robot = Robot()

    # Add to planet
    planet.add_human(human)
    planet.add_robot(robot)

    # Display current inhabitants
    print(planet.humans)
    print(planet.robots)