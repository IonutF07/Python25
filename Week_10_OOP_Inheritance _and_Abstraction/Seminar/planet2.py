# Define the Planet class which can hold humans and robots
from human1 import Human
from robot1 import Robot

class Planet:

    def __init__(self):
        self.inhabitants = []

    def __repr__(self):# Developer-friendly representation
        return f"planet(inhabitants={self.inhabitants})"

    def __str__(self):# User-friendly representation
        return f"This planet has {len(self.inhabitants)} inhabitants"

    def add(self, inhabitant):# Add a human object to the humans list
        self.inhabitants.append(inhabitant)

    def remove(self, inhabitant):# Remove a human object from the humans list
        self.inhabitants.remove(inhabitant)

