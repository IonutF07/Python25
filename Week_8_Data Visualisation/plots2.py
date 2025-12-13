#Squares with line plot
import matplotlib.pyplot as plt

def small():
    # Plotting a small square red dotted line and circle markers.
    # Specific numbers that form a small square
    x = [4, 3, 2, 3, 4]
    y = [4, 3, 3, 4, 4]
    # 'r:o' means: red colour (r), dotted line (:), circle markers (o)
    plt.plot(x, y, 'r--s')


def medium():
    # Plot a medium square using a green dashed line and square markers.
    x = [4, 3.5, 4, 4.5, 4]
    y = [4, 5, 6, 5, 4]
    # 'g--s' means: green (g), dashed line (--), square markers (s)
    plt.plot(x, y, 'b-p')


def large():
    # Plot a large square using a blue solid line and pentagon markers.
    x = [4, 5, 6, 5, 4]
    y = [4, 4, 3, 3, 4]
    plt.plot(x, y, 'g--p') # 'b-p' means: blue (b), solid line (-), pentagon markers (p)

def run_task2():
    small()
    medium()
    large()
    # Show the combined plot
    plt.show()

if __name__ == "__main__":
    run_task2()