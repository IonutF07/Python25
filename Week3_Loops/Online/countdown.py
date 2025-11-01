#Ask the user for the number of steps to the target

steps = int(input("How far are you from the target (in steps)?"))
#use a for loop to count down the steps
for step in range(steps, 0, -1):
    print(f"{step} steps remaining...")
    if step == 1:
        print("1 step remaining...")
#display the final message
print("You have reached the target!")