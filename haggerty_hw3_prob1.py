# Author: Parker Haggerty
# Date: 2/14/17
# Assignment 3, Problem 1

# Import stuff!
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Read in file
data = open(stm.txt, r)

# Plot plot plot plot...
gaussian_kde(data)
xs = np.linspace(0,8,200)
density.covariance_factor = lambda : .25
density._compute_covariance()
plt.plot(xs,density(xs))
plt.show()