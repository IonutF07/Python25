# This program removes a specified number of obstacles
count_str = input("How many obstacles should I avoid?\n")

target = int(count_str) #convert the string to an integer
avoided = 1 #initialize a counter for removed obstacles

#loop until we have removed the target number of obstacles
while avoided <= target:
    print(f"Avoiding...Done {avoided} obstacle avoided")
    avoided = avoided + 1  # increment the counter
print("All obstacles have been avoided.")
