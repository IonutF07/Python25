#Writting a class with a method to display attributes
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        # Method to display the attributes
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}")
p1 = Person("Ionut", 29, 76)
p1.display()



