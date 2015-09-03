import numpy as np
import math
import scipy as sp
from matplotlib import pyplot as plt

## Problem 1 ## 
def Newton(func, error, maxiter, guess, prime = None):
    h = 1e-6
    converge = True
    iterations = 0
    change = np.inf 
    x0 = guess
    def NoPrime(xold, func):
        deriv = (func(xold+h)-func(xold))/h
        return xold - func(xold)/deriv
    def WithPrime(xold, func, prime):
        return xold-(func(xold)/prime(xold))
    xnew = -10. 
    while np.any(change -  error > 0 ):
        if prime is None:
            xnew = NoPrime(x0, func)
            iterations += 1 
            change = abs(x0 - xnew)
            x0 = xnew
            if iterations >= maxiter:
                converge = False
                print ('Convergence: False')
                return xnew

        else:
            xnew = WithPrime(x0, func, prime)
            iterations += 1
            print iterations
            change = abs(x0 - xnew)
            x0 = xnew
            if iterations >= maxiter:
                converge = False
                print ('Convergence: False')
                return xnew
            
    print ('convergence: {} Error: {} Iterations: {}'.format(converge, change, iterations))
        
    return xnew

def f1(x):
    return np.cos(x)
def f1prime(x):
    return -np.sin(x)
def f2(x):
    return x**2*np.sin(1/x)
def f2prime(x):
    return 2*x*np.sin(1/x)-np.cos(1/x)
def f3(x):
    return (np.sin(x)/x)-x
def f4(x):
    return x**2-1
def f5(x):
    return x**3-x
def f6(x):
    return x**(1/3)
small = 1e-10
print Newton(f1,.0000000001,  10, 1, f1prime )
print Newton(f2, small, 10, 1, f2prime)
print Newton(f3, small, 10, 1, None)
print Newton(f4, small, 10, 2, None)
print Newton(f5, small, 10, 2, None)



print Newton(f4, small, 10, -2, None)
print Newton(f4, small, 10, -2, None)
#print Newton(f6, small, 10, 1)

### Problem 2 ###

def polyJulia(p, realmin, realmax, imin, imax, 
        maxiter = 200, res = 500, tol = 1e-5):
    r = 3
    roots = p.roots
    roots = np.around(roots, r)
    x = np.linspace(realmin, realmax, res)
    y = np.linspace(imin, imax, res)
    X,Y = np.meshgrid(x,y)
    deriv = p.deriv()
    c1 = Newton(p, tol, maxiter, X+1j*Y,  deriv)
    c2 = np.around(c1, r)
    for i, root in enumerate(roots):
        c2[c2==root]=i+10
    s1 = set(c2.flatten())
    print s1
    
    plt.pcolormesh(X,Y,c2)
    plt.show()

p1 = np.poly1d([1,-2,-2,2])
p2 = np.poly1d([3,-2,-2,2])
p3 = np.poly1d([1,3,-2,-2,2])
p4 = np.poly1d([1,0,0,-1])

polyJulia(p1, -.5, 0, -.25, .25)
polyJulia(p2, -1, 1, -1, 1)
polyJulia(p3, -1, 1, -1, 1)
polyJulia(p4, -1, 1, -1, 1)



### Problem 3 ####


x = np.linspace(-1.5,.5, 500)
y = np.linspace(-1, 1, 500)
X,Y = np.meshgrid(x,y)
C = X + 1j*Y
xold = C.copy()
xnew = np.zeros_like(C, dtype = int)
for i in xrange(30):
    try:
        xold = xold * xold + C
    except:
        pass
    xnew[np.real(xold) < 1e10] += 1
plt.pcolormesh(X,Y, xnew)
plt.show()


