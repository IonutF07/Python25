#Vehicle is the parent class
class Vehicle:
    def move(self):
        print("The vehicle is moving")

#Car is the child class
#Car inherits the move() method from Vehicle
class Car(Vehicle):
    def drive(self):
        print("The car is driving")


# Create an object of the child class
car1 = Car() # object is being created call car1
#An object of Car can use both parent and child methods

# Call the methods
car1.move()     # inherited from Vehicle
car1.drive()    # defined in Car

#NOTE: Methods only run when they are called using an object.
