#Creating a class
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
# Creating an instance of the Person class
p1 = Person("Ionut", 29, 76)
print(f"Name: {p1.name}, Age: {p1.age}, Weight: {p1.weight}")



