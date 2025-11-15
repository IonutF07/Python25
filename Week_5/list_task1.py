#Simple list - Store Maze Directions
def directions(): #Define a function called directions.
    #create a list of maze directions
    steps = ["Move forward","Move backward","Turn Left","Turn Right"]
    return steps #return complete list of steps
def run_task1():
    maze_steps = directions() # Get the list of directions by calling the directions function.
    print(maze_steps) # Print the entire list of directions.
#Ensure task1 runs when this script is executed
if __name__ == "__main__":
    run_task1()