#plt.pie - This function is used to create a pie chart.

import matplotlib.pyplot as plt

labels = ('A', 'B', 'C', 'D')
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels,autopct='%1.1f%%') #autopct='%1.1f%%' adds percentage values to each slice
plt.show()
plt.show()