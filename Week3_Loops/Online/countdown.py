#Ask the user for the number of steps to the target
print("How far are you from the target (in steps)?")
steps = int(input())
#use a for loop to count down the steps
for step in range(steps, 0, -1):
    print(f"Step {step}")
#display the final message
print("You have reached the target!")