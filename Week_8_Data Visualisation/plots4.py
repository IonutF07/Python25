#Data dictionary and Plots
import matplotlib.pyplot as plt
import random as rnd

def data():
    # Dictionary to store the user's plotting choices
    paths = {}
    # User input choose a line style
    print("What type of line (:, -- or -)?")
    line_style = input()
    # User input choose a colour
    print("What colour (r, g or b)?")
    colour = input()
    # User input  choose a style marker
    print("What type of marker (o, s or ^)?")
    marker_style = input()

    # Store chosen values in the dictionary
    paths["line_style"] = line_style
    paths["colour"] = colour
    paths["marker_style"] = marker_style

    # Return the completed dictionary
    return paths

def generate():
    # Ask how many lines the user would like to display
    print("How many lines would you like to display?")
    num_lines = int(input())
    # Create the requested number of lines
    for _ in range(num_lines):
        # Get a dictionary of style settings for this line
        values = data()
        # Generate 5 unique random integers from 1 to 9 for x and y values
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        # Build the matplotlib format string (e.g., "r--o")
        fmt = f"{values['colour']}{values['line_style']}{values['marker_style']}"
        # Plot the line using the random points and the chosen style
        plt.plot(x, y, fmt)
    # Show all lines together in one plot window
    plt.show()

def run_task4():
    # Task runner: show start message, generate the plot(s), then show end message
    print("Running...")
    generate()
    print("Done!")

if __name__ == "__main__":
    run_task4()