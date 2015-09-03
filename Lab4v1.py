#problem 1
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg as la
from scipy import sparse 
from scipy.sparse import linalg as sl
# Single ``for'' loop
def func1(n):
    n = 500*n
    sum(xrange(n))

# Double ``for'' loop
def func2(n):
    n = 3*n
    t = 0
    for i in xrange(n):
        for j in xrange(i):
            t += j


# Square a matrix
def func3(n):
    n = int(1.2*n)
    A = np.random.rand(n, n)
    np.power(A, 2)


# Invert a matrix
def func4(n):
    A = np.random.rand(n, n)
    la.inv(A)


# Find the determinant of a matrix.
def func5(n):
    n = int(1.25*n)
    A = np.random.rand(n, n)
    la.det(A)

"""
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

plt.legend(loc = 'upper left')
plt.show()


###################### Problem 2 #######################

#Part 1

def Sparse(n):
    """
    Takes in an integer, n, and returns an nxn sparse matrix with 2's
    on the main diagonal and -1's on the diagonals directly above, 
    and below the main diagonal. 
    """
    one = np.array(np.tile([-1],(1,n)))
    two = np.array(np.tile([2],(1,n)))
    data = np.reshape(np.array([one, two, one]),(3,n))
    diags = np.array([-1, 0, 1])
    A = sparse.spdiags(data, diags,  n, n, format = "csr")
    return A

A=Sparse(5)

#Part 2

def randmatrixsolver (n):
    """
    Takes in an integer, n, and builds 1xn random vector, then solves the
    system of the sparse nxn matrix Ax=b, and returns the vector x.
    """
    b=np.random.rand(n,1)
    A = Sparse(n)    
    return sl.spsolve(A,b) 

randmatrixsolver (5)



################### Problem 4 ###########################

def Eigensolver(n):
    """
    Takes n, returns lambda*n**2 where lambda is the smalles eigen value, 
    and n is obviously the dimension of the nxn tri-diagonal, sparse 
    matrix we caluclated in Problem 2. 
    """
    A = Sparse(n)
    lam, B = sl.eigs(A.asfptype(), k = 1, which = "SM")
    return np.real(lam)*n**2
Eigen = Eigensolver(10)
print Eigen

### Seems to be approaching e**.5 as n approaches infinity ###

