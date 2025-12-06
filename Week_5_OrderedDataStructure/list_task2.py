#Indexing - Directions with steps
def movements(): #Define a function called movements.
    #create a function called movements
    movements = ["Move forward",10,"Move backward",5,"Turn Left",3,"Turn Right",1]
    return movements #return complete list of steps
def run_task2():
    print("Moving..") # Print Moving...
    route = movements() # Get the list of directions by calling the movements function.
    for index in range(0, len(route), 2): #loop through the list with a step of 2
        direction = route[index] #get the direction at the current index
        step_count = route[index + 1] #get the step count at the next index
        print(f"{direction} for {step_count} steps") #print the direction with its corresponding step count
#Ensure task1 runs when this script is executed
if __name__ == "__main__":
    run_task2()