from robot1 import Robot
from human1 import Human
from planet2 import Planet

if __name__ == "__main__":
    robot = Robot()
    print(repr(robot))
    robot.move(10)
    print(repr(robot))
    robot.eat(5)
    print(repr(robot))
    print("\n")
    human = Human()
    print(repr(human))
    human.move(50)
    print(repr(human))
    human.eat(25)
    print(repr(human))
    print("\n Planet inheritance")
    planet = Planet()
    print(repr(planet))
    prins = Human("Prins")
    JamesBOT = Robot("JamesBOT")
    planet.add(JamesBOT)
    planet.add(prins)
    planet.add(robot)
    planet.add(human)

    print(repr(planet))
    print(planet)