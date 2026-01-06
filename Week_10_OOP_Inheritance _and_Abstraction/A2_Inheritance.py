#Person is the parent class
class Person:
    def speak(self):
        print("I can speak")

    def walk(self):
        print("I can walk")

#Student is the child class
#Student inherits speak() and walk() from Person
class Student(Person):
    def study(self):
        # study() belongs only to Student

        print("I am studying")

#creating student1 allows access to both parent and child methods

# Using the Child Class
student1 = Student() # creating object call student1
student1.speak()   # inherited from Person
student1.walk()    # inherited from Person
student1.study()   # own method
