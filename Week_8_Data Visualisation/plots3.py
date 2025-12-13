#Path with Line Plots
import matplotlib.pyplot as plt

def coordinate():
    # Ask the user for one x value, then one y value, and return them as a tuple (x, y)
    print("Please enter an x value:")
    x = int(input())
    print("Please enter a y value:")
    y = int(input())
    return (x, y)

def path():
    # Collect 4 coordinate points from the user and store them in two separate lists
    print("Retrieving path...")
    x_values = []  # store all x values here
    y_values = []  # store all y values here

    # Repeat 4 times to build a 4-point path
    for r in range(4):
        x, y = coordinate()   # unpack returned tuple
        x_values.append(x)    # add x to the x list
        y_values.append(y)    # add y to the y list
    # Return both lists in a single list (to match the solution approach)
    return [x_values, y_values]

def run_task3():
    # Build the path (two lists: x list and y list), then plot it
    values = path()
    # Plot the path using a red dashed line with circle markers
    plt.plot(values[0], values[1], "r--o")
    # Add axis labels (good practice for readability)
    plt.xlabel("x values")
    plt.ylabel("y values")
    # Display the plot window
    plt.show()

if __name__ == "__main__":
    run_task3()