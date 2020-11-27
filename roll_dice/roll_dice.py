# Import Modules
import numpy as np
from matplotlib import pyplot

# Generate the list of random numbers
# For plot 1
random_list = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6]
# For plot 2
N = 100  # number of data points, i.e. number of numbers in the list
x = np.random.randint(1, 7, N)

# Plot 2 histograms
b = 6  # number of bins in the histogram
fig, axs = pyplot.subplots(2, 1, sharex=True)
axs[0].hist(x, bins=b)
axs[1].hist(random_list, bins=b)
pyplot.show()
