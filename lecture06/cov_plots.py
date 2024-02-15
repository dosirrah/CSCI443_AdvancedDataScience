
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

#x = [-1, -1, -.5, 0, 0, -.5, .5, .5, 1, 1]
#y = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
#x = [-1, 1]
#y = [1, -1]
#x = [-1, -.5, 0, .5, 1]
#y = [-1, -.5, 0, .5, 1]
x = [-1, -1, 1, 1]
y = [1, -1, 1, -1]

# Create the plot
plt.stem(x, y, '-.')

# set range of the x- and y-axes.
plt.xlim([-1.1, 1.1])
plt.ylim([-1.1, 1.1])

# Get the current axes
ax = plt.gca()

# Hide the top and right spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Move the bottom spine to y=0
ax.spines['bottom'].set_position(('data', 0))

# Move the left spine to x=0
ax.spines['left'].set_position(('data', 0))

# Adjust the ticks so they're on the left and bottom only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()

