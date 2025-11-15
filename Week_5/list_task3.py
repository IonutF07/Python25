#Iterate - Build a menu from a list
def directions(): #Define a function called directions.
    #create a list of directions
    steps = ["Move forward","Move backward","Turn Left","Turn Right"]
    return steps #return complete list of steps
def menu():#
    #Display menu options
    print("Please select a direction:")
    steps = directions() # Get the list of directions by calling the directions function.
    for index in range (len(steps)):
        direction = steps[index]
        print(f"{index}:{direction}") 
def run_task3():
    menu() # Display the menu
#Ensure task3 runs when this script is executed
if __name__ == "__main__":
    run_task3()