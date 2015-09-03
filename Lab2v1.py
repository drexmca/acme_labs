# All import statements always belong at the top of your code.
# Standard libraries go first.
import math
from random import normalvariate
import random
import itertools

# Other libraries are second.
from scipy.misc import factorial
import numpy as np
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


"""
Problem 1
To do 2x2 matrix multiplication in numpy, just do numpy.dot(M1,M2) on two numpy arrays.
"""
print ("Problem 2") # Don't put a space here.  That's a violation of pep 8.  
# see https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements
print("Exercise 1")
def normal(n):
    """
    Docstrings are important for coding.
    """
    m=np.zeros((n,n))
    for i,j in itertools.product(range(n), range(n)):
        m[i][j]=normalvariate(0,1)
    return m

normal (100)
print("Exercise 2") # This should be part of the normal funtion and it's output.
m=normal(3)
mean = m.mean()
print (mean)
# Put a blank line or two between exercises

print ("Exercise 3")
variance = m.var()
print (variance)

#As you increase the number n, mean will approach 0, var will approach 1.... not suprising

print ("Press any key")
raw_input() # These were very helpful.  Good job.
print("Problem 3")

def laplace (m,tol):
    """
    Use a docstring to explain what m and tol are.
    """

    dif = 1 # This should be the tolerance parameter.
    
    copym=np.copy(m)
    print(copym)
    copym[1:-1,1:-1]=(copym[:-2,1:-1]+copym[2:,1:-1]+
            copym[1:-1,2:]+copym[1:-1,:-2])/4
    print (copym) # That space has got to go!
    A=m-copym # This line could use the extra space.
    # A = m-copym # This line could use the extra space.
    print (A) # Extra print statements in the code are really annoying.
    A=np.absolute(A)
    print (A)
    dif = np.amax(A)
    print (dif,tol)
    while dif >=tol:
        copym1=np.copy(copym)
        copym1[1:-1,1:-1]=(copym1[:-2,1:-1]+copym1[2:,1:-1]+
                copym1[1:-1,2:]+copym1[1:-1,:-2])/4
        A=np.absolute(copym1)-np.absolute(copym)
        dif = np.amax(A)
        copym=copym1
    return copym

a=np.random.rand(6,6)
a=laplace(a,.001)

n = 100
tol = .0001
U = np.ones ((n, n))
U [:,0] = 100 #sets north boundary condition
U [:,-1] = 100 # sets south boundary condition
U [0] = 0 # sets west boundary condition
U [-1] = 0 # sets east boundary condition
# U has been changed in place (note that laplace is the name of
# the function in this case).

U = laplace(U, tol)
x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot_surface (X, Y, U, rstride=5)
plt.show()

print ("Press any key")
raw_input()
print ("Problem 4")

a=np.random.randint(0,256,[100,100,3])
b=np.ones([1,1,3])
c = np.array([.5,.5,1])
d=b*c
e = a*d

print(a)
print(d)
print(e)

#Exercise 5 Have it print that this is exercise five.
#part 1

def arcsin(n,x):
    #construct a backwards order of your n's
    integers = np.arange(n,-1,-1, dtype=np.float64)
    coeff = factorial(integers*2)/((2*integers+1)*(factorial(integers)**2)*(4**integers))
    allcoeff = np.zeros(2*n+2)
    allcoeff[::2]=coeff[:]
    return np.polyval(allcoeff,x)

pi = 4*arcsin(10,1/(np.sqrt(2)))
print(pi)

#part 2
def W (n):
    integers = np.arange(n,0,-1, dtype=np.float64)
    coeff = (-integers)**(integers-1)/(factorial(integers))
    allcoeff=np.poly1d(np.append(coeff,0))
    return allcoeff(.25)

a=W(70)
print(a*math.e**a)

