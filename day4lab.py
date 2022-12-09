 
# Program to plot a simple graph
#
# WWritten by Ben Wheeler
# Culver-Stockton College    2/7/2018
#
from matplotlib.pylab import plot, show, title, xlabel, ylabel
# Make a list of x coordinates
x = [1, 2, 3, 4, 5]
title("Car Wash Graph ")
xlabel("Time (PM) ")
ylabel("Cars in Line ")
# Make a list of y coordinates
y = [8,10,6,0,3]
plot (x,y)
# Produce a graph
show()

