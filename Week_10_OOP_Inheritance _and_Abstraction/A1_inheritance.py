# Inheritance is an OOP concept where a class (called child/subclass) can reuse attributes and methods from another class (called parent/superclass).
# Reduces code duplication
# Helps create a hierarchy of classes

# Parent class
class Parent:
    # Parent is a parent (base) class
    # It defines a method called greet()
    def greet(self):
        # When greet() is called, it prints:
        print("Hello from Parent class")

# Child Class (Inheritance)
class Child(Parent):#Child is a child (derived) class
    def hello(self):
        # Inherits the greet() method
        # Has its own method hello()
        print("okay here")

#Creating an Object of the Child Class
c = Child()

#An object named c is created from the Child class
# Because of inheritance, c has access to:
#greet() (from Parent)
#hello() (from Child)

#Calling an Inherited Method
c.greet()   # Output: Hello from Parent

 # Calls the greet() method defined in the Parent class
 # Even though greet() is not written inside Child, it works because of inheritance
