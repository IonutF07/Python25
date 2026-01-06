# Step 1: Abstract Parent Class

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    # You cannot create an object from Animal.


# Step 2: Child Class

class Dog(Animal):
    def sound(self):
        print("The dog barks")

    # Step 3: Create Object and Display Output


dog1 = Dog()
# Step 4: Call the methods
dog1.sound()