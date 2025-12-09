# This function takes two parameters; "plt.plot"
# a list of values representing points on the x-axis and a list of values representing points on the y-axis.
# The function draws these points (markers) on a graph and then joins them up using a line.
# The function is used to create line graphs or display markers.

#Ploting a straight line
import matplotlib.pyplot as plt

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("x values")
plt.ylabel("y values")

plt.plot(x, y)
plt.show()

#Ploting with a marker and points

import matplotlib.pyplot as plt

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("x values")
plt.ylabel("y values")

plt.plot(x, y,marker=,"o") #Adding the marker draws a line between the points