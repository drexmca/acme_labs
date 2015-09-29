# spec.py
"""Volume I Lab 5: Invertible Affine Transformations and Linear Systems.
Name: Rex McArthur
Date: Sept. 29, 2015
"""

# include your import statements here.
import numpy as np
from scipy import linalg as la
import matplotlib.pyplot as plt
import time

# Helper Functions
def plot_transform(original, new):
    """Display a plot of points before and after a transform.
    
    Inputs:
        original (array) - Array of size (2,n) containing points in R2 as columns.
        new (array) - Array of size (2,n) containing points in R2 as columns.
    """
    window = [-5,5,-5,5]
    plt.subplot(1, 2, 1)
    plt.title('Before')
    plt.gca().set_aspect('equal')
    plt.scatter(original[0], original[1])
    plt.axis(window)
    plt.subplot(1, 2, 2)
    plt.title('After')
    plt.gca().set_aspect('equal')
    plt.scatter(new[0], new[1])
    plt.axis(window)
    plt.show()

def type_I(A, i, j):  
    """Swap the i-th and j-th rows of A."""
    A[i], A[j] = np.copy(A[j]), np.copy(A[i])
    
def type_II(A, i, const):  
    """Multiply the i-th row of A by const."""
    A[i] *= const
    
def type_III(A, i, j, const):  
    """Add a constant of the j-th row of A to the i-th row."""
    A[i] += const*A[j]

points = np.load("pi.npy")

# Problem 1
def dilation2D(A, x_factor, y_factor):
    """Scale the points in A by x_factor in the x direction and y_factor in
    the y direction. Returns the new array.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        x_factor (float) - scaling factor in the x direction.
        y_factor (float) - scaling factor in the y direction.
    """
    dilate = np.diag(np.array([x_factor, y_factor]))
    return dilate.dot(A)

#plot_transform(points, dilation2D(points, 1.5,1))

    
# Problem 2
def rotate2D(A, theta):
    """Rotate the points in A about the origin by theta radians. Returns 
    the new array.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        theta (float) - number of radians to rotate points in A.
    """
    """
    This function is designed to plot a linear transformation rotation around the 
    origin.
    ## Paramaters ##
    circle: 2xn array to plot
    theta: angle you want to roatate about the origin
    """
    rmatrix = np.zeros((2,2))
    rmatrix[0][0] = np.cos(theta)
    rmatrix[0][1]= -np.sin(theta)
    rmatrix[1][0] = np.sin(theta)
    rmatrix[1][1] = np.cos(theta)
    return rmatrix.dot(A)

#plot_transform(points, rotate2D(points, np.pi/4.))
    
# Problem 3
def translate2D(A, b):
    """Translate the points in A by the vector b. Returns the new array.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        b (2-tuple (b1,b2)) - Translate points by b1 in the x direction and by b2 
            in the y direction.
    """
    newdata = np.copy(A)
    shift = np.vstack([b[0], b[1]])
    return newdata + shift

#plot_transform(points, translate2D(points, [1., 2.]))
   
# Problem 4
def calc_p2(time, omega, direction, speed):
    p1 = np.array([1,0])
    p2 = np.array([0,0])
    p2 = np.multiply(direction, ((speed*time)/(np.linalg.norm(direction))))
    p1 = rotate2D(p1, time*omega)
    p1 = np.array([[p1[0],p1[1]]])
    p1 = translate2D(p1.T, p2)
    return p1

def rotatingParticle(time,omega,direction,speed):
    """Display a plot of the path of a particle P1 that is rotating 
    around another particle P2.
    
    Inputs:
     - time (2-tuple (a,b)): Time span from a to b seconds.
     - omega (float): Angular velocity of P1 rotating around P2.
     - direction (2-tuple (x,y)): Vector indicating direction.
     - speed (float): Distance per second.
    """
    t = np.linspace(time[0], time[1], 100)
    pos = np.zeros((2,len(t)))
    for i in xrange(len(t)):
        pos[:,i]=calc_p2(t[i],omega, direction, speed).flatten()
    plt.axis([0,16, 0,16])
    plt.plot(pos[0], pos[1])
    plt.show()
    pass

# Problem 5
def swap(A, i, j):
    A[i],A[j] = np.copy(A[j]),np.copy(A[i])
    return A

def mult(A, i, const):
    A[i] *= const
    return A

def addup(A, i, j, const):
    A[i] += const*A[j]
    return A

def REF(A):
    """Reduce a square matrix A to REF. During a row operation, do not
    modify any entries that you know will be zero before and after the
    operation. Returns the new array."""
    column = 0
    dim = len(A[0][:])
    operations = dim - 1
    X = 0
    Y = 0
    for x in xrange(dim):
        for y in range(Y, operations):
            operator = -A[y+1][x]/A[X][x] 
            print 'Operator: ', operator
            A = addup(A, y+1, X, operator)
        Y+=1
        X+=1
    return A
rowmatrix = np.array([[4.,5.,6.,3.],[2.,4.,6.,4.],[7.,8.,0.,5.],[1.,2.,6.,4.]])
print REF(rowmatrix)
    
# Problem 6
def LU(A):
    """Returns the LU decomposition of a square matrix."""
    m,n = np.shape(A)
    U = np.copy(A)
    L = np.eye(n)
    for i in xrange(1,n):
        for j in xrange(i):
            L[i,j] = U[i,j]/U[j,j]
            U[i,j:] = U[i,j:] - np.dot(L[i,j], U[j,j:])
    return L, U
rowmatrix = np.array([[4.,5.,6.,3.],[2.,4.,6.,4.],[7.,8.,0.,5.],[1.,2.,6.,4.]])
L, U = LU(rowmatrix)
print 'L', L
print 'U', U
print 'A', np.dot(L,U)

# Problem 7
def time_LU():
    """Print the times it takes to solve a system of equations using
    LU decomposition and (A^-1)B where A is 1000x1000 and B is 1000x500."""
    A = np.random.random((1000,1000))
    b = np.random.random((1000,500))
    start = time.time()
    L = la.lu_factor(A)
    a = time.time() - start
    start = time.time()
    A_inv = la.inv(A)
    a2 = time.time() - start
    start = time.time()
    la.lu_solve(L,b)
    a3 = time.time() - start
    start = time.time()
    np.dot(A_inv, b)
    a4 = time.time() - start

    
    time_lu_factor = a  # set this to the time it takes to perform la.lu_factor(A)
    time_inv = a2 # set this to the time it takes to take the inverse of A
    time_lu_solve = a3  # set this to the time it takes to perform la.lu_solve()
    time_inv_solve = a4  # set this to the time it take to perform (A^-1)B


    print "LU solve: " + str(time_lu_factor + time_lu_solve)
    print "Inv solve: " + str(time_inv + time_inv_solve)
    
    # What can you conclude about the more efficient way to solve linear systems?
    print "Better to use LU decomposition than inverse, cause it is NEVER a good idea to calculate an inerse"  # print your answer here.
time_LU()
    

