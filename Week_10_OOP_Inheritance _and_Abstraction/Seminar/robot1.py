from inhabitant import Inhabitant

class Robot(Inhabitant):

    laws = "Protect, Obey and Survive"

    @staticmethod
    def the_laws():
        print(Robot.laws)

    def __init__(self, name="Robot", age=0):
        super().__init__(name, age)

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

    def display(self):
        print(f"I am {self.name}")