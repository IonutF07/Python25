#Squares with line plot
import matplotlib.pyplot as plt

def small():
    # Plotting a small square red dotted line and circle markers.
    # Specific numbers that form a small square
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]
    plt.plot(x, y, 'r:o') # 'r:o' means: red colour (r), dotted line (:), circle markers (o)

def medium():
    # Plotting a medium square green dashed line and square markers.
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]
    plt.plot(x, y, 'g--s') # 'g--s' means: green (g), dashed line (--), square markers (s)

def large():
    # Plotting a large square blue solid line and pentagon markers.
    x = [1, 1, 6, 6, 1]
    y = [1, 6, 6, 1, 1]
    plt.plot(x, y, 'b-p') # 'b-p' means: blue (b), solid line (-), pentagon markers (p)

def run_task2():
    small()
    medium()
    large()
    # Show the combined plot
    plt.show()

if __name__ == "__main__":
    run_task2()