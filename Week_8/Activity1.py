#Sets do not allow duplicate values:
my_set = {1, 2, 3, 4, 4, 5}
print(my_set) # Output: {1, 2, 3, 4, 5}

#Add itemes to a set using the add() method:
my_set.add(6)
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

#Remove items from a set using the remove() method:
my_set.remove(3)
print(my_set) # Output: {1, 2, 4, 5, 6}

#Check if an item is in a set using the in keyword:
print(4 in my_set) # Output: True
print(3 in my_set) # Output: False

#Printing lenght of a set using len() function:
print(len(my_set)) # Output: 5