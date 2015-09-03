from scipy import sparse
from scipy import linalg as la
import timeit
import time
import random
import cymodule
import numpy as np

## Problem 1 ##



def slowsum(a,b):
    """
    Sums all numbers starting at a, and going to b
    """
    x=0
    for i in range(a,b):
        x = x+i
    return x

def fastsum(a,b):
    """
    More efficently sums the numbers in range a,b
    """
    return sum(xrange(a,b))

# I eliminated the for loop, and used xrange instead of range.
# This changed the time to run each loop from 75.7 microsec, to 
# 17 micro seconds. 

### Problem 2 ###

def pysum(X):
    """
    Return the sum of the elements of X.
    Inputs:
    x - a 1-D NumPy array
    """
    summ = 0
    for i in range(len(X)):
        summ = summ+X[i]
    return summ

x = np.array(range(int(1e4)))

print ("Cython")
start = time.time()
cymodule.cypysum(x)
print time.time() - start

print ("Python")
start = time.time()
pysum(x)
print time.time() - start

print ("Simple Cython")
start = time.time()
cymodule.cysum_p(x)
print time.time() - start



### Problem 3 ### 
def pymatpow(X, power):
    ''' Return X^{power}.
    INPUTS:
    X
    - A square 2-D NumPy array
    power
    - An integer
    '''
    prod = X.copy()
    temparr = np.empty_like(X[0])
    size = X.shape[0]
    for n in xrange(1, power):
        for i in xrange(size):
            for j in xrange(size):
                tot = 0.
                for k in xrange(size):
                    tot += prod[i,k] * X[k,j]
                temparr[j] = tot
            prod[i] = temparr
    return prod

A = np.random.random_integers(100, size = (100,100))
print ("Problem 3")
print ("Python Product")
start = time.time()
pymatpow(A, 2)
print time.time() - start

print ("Cython Product")
start = time.time()
cymodule.pymatpow(A, 2)
print time.time() - start

print ("Numpy dot product")
start = time.time()
np.dot(A,A)
print time.time() - start

### Problem 5 ###
print ("Problem 5")
def pytridiag(a, b, c, x):
    '''Solve the tridiagonal system Ad = x where A has diagonals
    a, b, and c.
    INPUTS:
        a, b, c, x - All 1-D NumPy arrays.
        NOTE:
            The final result is stored in `x` and `c` 
            is used to store temporary values.
            '''
    n = x.size
    temp = 0.
    c[0] /= b[0]
    x[0] /= b[0]
    for i in xrange(n-2):
        temp = 1. / (b[i+1] - a[i] * c[i])
        c[i+1] *= temp
        x[i+1] = (x[i+1] - a[i] * x[i]) * temp
    x[n-1] = (x[n-1] - a[n-2] * x[n-2]) / (b[n-1] - a[n-2] * c[n-2])
    for i in xrange(n-2, -1, -1):
        x[i] = x[i] - c[i] * x[i+1]

  
a = np.random.random(100000)
b = np.random.random(100000)
c = np.random.random(100000)
x = np.random.random(100000)

pytridiag(a,b,c,x)
print ("Python")
start =time.time()
pytridiag(a,b,c,x)
print time.time() - start

print ("Cython")
start = time.time()
cymodule.pytridiag(a,b,c,x)
print time.time() - start 

a = np.random.random((100,100))
b = np.random.random((100,100))
print ("Scipy")
start = time.time()
la.solve(a,b)
print time.time() - start


# You can have good algorithims, but bad implementation screws it up.






