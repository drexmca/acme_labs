from __future__ import division
import numpy as np
import math
from matplotlib import pyplot as plt

### Problem 1 ###

def Simpson(f, a, b):
    a = ((b-a)/6.0)*sum(np.array([1,4,1])*f(np.array([a,(a+b)/2.0,
        b])))
    return a 

def Simpson38(f, a, b):
    return ((b-a)/8.0)*sum(np.array([1,3,3,1])*func(np.array([a,(2*a+b)/3.0,
        (a+2*b)/3.,b])))

def Boole(func, a, b):
    return ((b-a)/90.0)*sum(np.array([7,32,12,32,7])*func(np.array([a,
        (3*a+b)/4.0,(2*a+2*b)/4.,(a+3*b)/4.,b]))) 


### Problem 2 ###

def func(x):
	return x**(1./3.)

def EstSimpson(func, a, b, n):
    a1 = a
    estsum = 0
    for i in xrange(n):
        b1 = a1+(b-a)/(n)
        estsum = estsum + Simpson(func, a1, b1)
        a1 = b1
    return estsum 
	
def EstSimpson38(func, a, b, n):
    a1 = a
    estsum = 0
    for i in xrange(n):
        b1 = a1+(b-a)/(n)
        estsum = estsum + Simpson38(func, a1, b1)
        a1 = b1
    return estsum 


def EstBoole(func, a, b, n):
    a1 = a
    estsum = 0
    for i in xrange(n):
        b1 = a1+(b-a)/(n)
        estsum = estsum + Boole(func, a1, b1)
        a1 = b1
    return estsum 

print "Boole: ", EstBoole(func, 0., 1., 10)
print 'Simpson: ', EstSimpson(func, 0.,1.,10)
print 'Simpson38: ', EstSimpson38(func, 0., 1., 10)


### Problem 3 ###

def AdptSimpson(func, a, b, maxerror):
    estsum = 0
    error = np.inf
    subintervals = np.array([a,b])
    switch = True
    while switch == True:
	a1 = a
	estsum = 0
        n = len(subintervals)-1
        switch = False
	cerror = maxerror/n
        for i in xrange(n):
            a1 = subintervals[i]
            b1 = subintervals[i+1]
            c = (b1+a1)/2.
            error = abs(Simpson(func, a1, c)  + Simpson(func, c, b1) - 
                    Simpson(func, a1, b1))
            if error >= cerror:
	        subintervals = np.insert(subintervals, i+1, c)
	        switch = True
	    else:
		estsum = estsum + Simpson(func, a1, b1)

    return estsum, n 
"""
    for i in xrange(n):
        print subintervals
        estsum = estsum + Simpson(func, subintervals[i], 
                subintervals[i+1])
    return estsum
"""
estimate, iterations =  AdptSimpson(func, 0., 1., .00000001)
print 'Adpt Simpson: ', estimate, ' in ', iterations, ' iterations'
