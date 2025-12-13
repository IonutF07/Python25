#Simple Line Plot
import matplotlib.pyplot as plt

def display_line(x,y):#Display the plot for x and y
    plt.plot(x,y) #Drawing a basic line plot
    plt.show() #Render the plot window

def run_task1():
    #Task1 - creating a sample x and y data plot
    print("Running...")
    #Defining the x & y values (y is square of x)
    x_values = [1,2,3,4,5]
    y_values = [1,4,9,16,25]
    #Plot the data
    display_line(y_values,x_values)

if __name__ == "__main__":
    run_task1()