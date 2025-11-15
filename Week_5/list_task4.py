#Populate - Build an escape route with a list
def directions(): #Define a function called directions.
#create a list of directions
    steps = ["Move forward","Move backward","Turn Left","Turn Right"]
    return steps #return complete list of steps
def menu_and_input():
#Display menu options and get user input
    print("Please select a direction:")
    steps = directions() # Get the list of directions by calling the directions function.
    for index,direction in enumerate(steps):
        print(f"{index}:{direction}")
    choice_index = int(input()) # Get user input for choice
    return steps[choice_index] # Return the chosen direction
def run_task4():
#Build escape route by asking the user to select directions
    print ("Working out escape route...")
    escape_route = []
#Ask the user to choose a direction 5 times
    for _ in range(5):
        chosen_direction = menu_and_input()
        escape_route.append(chosen_direction)
    print(f"Your escape route is:{escape_route}")
#Ensure task4 runs when this script is executed
if __name__ == "__main__":
    run_task4()