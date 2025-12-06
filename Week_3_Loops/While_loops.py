#Ask the user for a number of apples to remove from a basket
#Use a while loop to remove that many apples, one at a time
count_str = input("How many apples should I remove?\n")

target = int(count_str) #convert the string to an integer
removed = 0 #initialize a counter for removed apples

#loop until we have removed the target number of apples
while removed < target:
    print(f"Removed apple.") #print the number of apples removed so far
    removed = removed + 1 #increment the counter
