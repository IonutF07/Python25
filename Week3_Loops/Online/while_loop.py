#Display the initial message
print("How many apples should I remove?")
#Read use response and convert to integer
total_apples = int(input())
#create a variable to keep track of removed apples
removed_apples = 0
#Use a while loop to remove apples until the desired number is reached
while removed_apples < total_apples:
    removed_apples += 1
    print(f"Removed {removed_apples} apple(s)")
#Display final message
print("All requested apples have been removed.")