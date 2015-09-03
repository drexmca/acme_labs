from __future__ import division
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

def mc_int(f, mins, maxs, numPoints=500, numIters=100):
    '''Use Monte-Carlo integration to approximate the integral of f
    on the box defined by mins and maxs.
    INPUTS:
    f - A function handle. Should accept a 1-D NumPy array
    as input.
    mins - A 1-D NumPy array of the minimum bounds on integration.
    maxs - A 1-D NumPy array of the maximum bounds on integration.
    numPoints - An integer specifying the number of points to sample in
    the Monte-Carlo method. Defaults to 500.
    numIters - An integer specifying the number of times to run the
    Monte Carlo algorithm. Defaults to 100.
    ALGORITHM:
    Run the Monte-Carlo algorithm `numIters' times and return the average
    of these runs.
    EXAMPLES:
    f = lambda x: np.hypot(x[0], x[1]) <= 1
    # Integral over the square [-1,1] x [-1,1] should be pi
    mc_int(f, np.array([-1,-1]), np.array([1,1]))
    3.1290400000000007
    '''
    integral = 0
    for i in xrange(numIters):
        Dimensions = len(maxs)
        points = np.random.rand(numPoints, Dimensions)
        points = mins + (maxs - mins) * points
        value = np.apply_along_axis(f,1,points)
        integral += np.prod(maxs - mins) * sum(value)/numPoints
    avg_integral = integral/numIters
    return avg_integral
f = lambda x: np.hypot(x[0], x[1]) <= 1
pi = mc_int(f, np.array([-1,-1]), np.array([1,1]), 1000, 200)
print pi

## Problem 2 ##
#Part 1
mins = np.array([-0.5, 0, 0, 0])
maxs = np.array([0.75, 1, 0.5, 1])
means = np.zeros(4)
covs = np.eye(4)
value, inform = stats.mvn.mvnun(mins, maxs, means, covs)
print value

#Part 2

def func(x):
    n = len(x)
    return 1/np.sqrt((2*np.pi)**n)*(np.exp(-x.dot(x)/2.))

trial = np.array([10, 100, 1000, 10000])
error = []
for i in trial:
    integral = mc_int(func, mins, maxs, numPoints = i)
    error.append(abs(integral-value))
    print integral

plt.plot(trial, error)
plt.show()


