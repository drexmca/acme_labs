import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg
from scipy import sparse
from scipy.sparse import linalg as sl

'''Functions for use in problem 1.'''
# Run through a single for loop.
def func1(n):
    n = 500*n
    sum(xrange(n))

# Run through a double for loop.
def func2(n):
    n = 3*n
    t = 0
    for i in xrange(n):
        for j in xrange(i):
            t += j

# Square a matrix.
def func3(n):
    n = int(1.2*n)
    A = np.random.rand(n, n)
    np.power(A, 2)

# Invert a matrix.
from scipy import linalg as la
def func4(n):
    A = np.random.rand(n, n)
    la.inv(A)

# Find the determinant of a matrix.
from scipy import linalg as la
def func5(n):
    n = int(1.25*n)
    A = np.random.rand(n, n)
    la.det(A)


def Problem1():
    """Create a plot comparing the times of func1, func2, func3, func4, 
    and func5. Time each function 4 times and take the average of each.
    n=100
    Single for loop: .887 ms per loop
    Double for loop: 3.34 ms per loop
    Square matrix: .547 ms per loop
    Invert matrix: 1.18 ms per loop
    Determinent: .937 ms per loop
    
    n=200
    Single for loop: 1.76  ms per loop
    Double for loop: 13.6  ms per loop
    Square matrix: 2.46 ms per loop
    Invert matrix: 6.05 ms per loop
    Determinent: 4.59 ms per loop
    
    n=400
    Single for loop: 3.53 ms per loop
    Double for loop: 56.3 ms per loop
    Square matrix: 10.1 ms per loop
    Invert matrix: 34.4 ms per loop
    Determinent: 24.7 ms per loop
    
    
    n=800
    Single for loop: 7.01 ms per loop
    Double for loop: 224 ms per loop
    Square matrix: 40.6 ms per loop
    Invert matrix: 225 ms per loop
    Determinent: 161 ms per loop
    
    """
    x = [100, 200, 400, 800]
    time1 = [.887, 1.76, 3.53, 7.01]
    time2 = [3.34, 13.6, 56.3, 224]
    time3 = [.547, 2.46, 10.1, 40.6]
    time4 = [1.18, 6.05, 34.4, 225]
    time5 = [.937, 4.59, 24.7, 161]
    
    plt.plot (x, time1, label="Func 1")
    plt.plot (x, time2, label="Func 2")
    plt.plot (x, time3, label="Func 3")
    plt.plot (x, time4, label="Func 4")
    plt.plot (x, time5, label="Func 5")
    
    #Func1 obviously has a simple complexity. It doesn't explode in growth
    #Func2 and Func3 grow faster, but not much
    #Func4, Func5 show the most spatially complex operations. 
    
    plt.legend(loc='upper left')
    plt.show()
    pass

def Problem2(n):
    """
    """
    one = np.array(np.tile([-1],(1,n)))
    two = np.array(np.tile([2],(1,n)))
    data = np.reshape(np.array([one, two, one]),(3,n))
    diags = np.array([-1, 0, 1])
    A = sparse.spdiags(data, diags,  n, n, format = "csr")
    return A

def Problem3(n):
    """Generate an nx1 random array b and solve the linear system Ax=b
    where A is the tri-diagonal array in Problem 2 of size nxn
    """
    b=np.random.rand(n,1)
    A = Problem2(n)    
    return sl.spsolve(A,b) 


def Problem4(n, sparse=False):
    """Write a function that accepts an integer argument n and returns
    (lamba)*n^2 where (lamba) is the smallest eigenvalue of the sparse 
    tri-diagonal array you built in Problem 2.
    """
    A = Problem2(n)
    lam, B = sl.eigs(A.asfptype(), k = n-2, which = "SM")
    min_lam = np.amin(lam)
    print 'Seems to be approaching pi**2 as n approaches infinity'
    return np.real(min_lam)*n**2

Problem1()
print Problem2(10)
print Problem3(10)
print np.sqrt(Problem4(500))

