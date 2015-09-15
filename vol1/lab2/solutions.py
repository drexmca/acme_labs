"""Volume 1 Lab 2: NumPy and SciPy
Written Summer 2015 (Tanner Christensen)
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# student's file should be called solutions.py

# Problem 1: Perform matrix multiplication
"""
Perform matrix-matrix multiplication on A and B.
Set the varibale 'product' to your answer.
"""
A = np.array(([[2,4,0],[-3,1,-1],[0,3,2]]))
B = np.array(([[3,-1,2],[-2,-3,0],[1,0,-2]]))
print A
print B
product = np.dot(A,B)  # set product equal to the result of AB.
print product

# Problem 2: Return an array with all nonnegative numbers

def nonnegative(my_array):
    """Changes all negative entries in the inputed array to 0 then returns
    the new array.

    Example:
    >>> my_array = np.array([-3,-1,3])
    >>> nonnegative(my_array)
    array([0,0,3])
    """
    A = my_array < 0
    my_array[A] = 0
    return my_array
#print nonnegative(np.array([-3,-1,3]))


# Problem 3: nxn array of floats and operations on that array

def normal_var(n):
    """Creates nxn array with values from the normal distribution, computes 
    the mean of each row and computes the variance of these means. Return this
    final value.
    """
    A = np.random.normal(0,1., (n,n))
    means = A.mean(axis = 1)
    var = means.var()
    return var

print normal_var(10) 

# Problem 4: Solving Laplace's Equation using the Jacobi method and array slicing
'''
def laplace(A, tol):
    """Solve Laplace's Equation using the Jacobi method and array slicing."""
    dif = 1
    copyA = np.copy(A)
    print(copyA)
    copyA[1:-1,1:-1]=(copyA[:-2,1:-1]+copyA[2:,1:-1]+
        copyA[1:-1,2:]+copyA[1:-1,:-2])/4
    print (copyA) # That space has got to go!
    A=A-copyA # This line could use the extra space.
    # A = m-copym # This line could use the extra space.
    print (A) # Extra print statements in the code are really annoying.
    A=np.absolute(A)
    print (A)
    dif = np.amax(A)
    print (dif,tol)
    while dif >=tol:
        copyA1=np.copy(copyA)
        copyA1[1:-1,1:-1]=(copyA1[:-2,1:-1]+copyA1[2:,1:-1]+
                     copyA1[1:-1,2:]+copyA1[1:-1,:-2])/4
        A=np.absolute(copyA1)-np.absolute(copyA)
        dif = np.amax(A)
        copyA=copyA1
    return copyA


def laplace (m,tol):
    """
    Use a docstring to explain what m and tol are.
    """

    dif = tol
    copym = np.copy(m)
    #copym[1:-1,1:-1]=(copym[:-2,1:-1]+copym[2:,1:-1]+
            #copym[1:-1,2:]+copym[1:-1,:-2])/4
    #m = m-copym 
    #m = np.absolute(m)
    #dif = np.amax(m)
    while dif >=tol:
        copym[1:-1,1:-1]=(copym[:-2,1:-1]+copym[2:,1:-1]+
                copym[1:-1,2:]+copym[1:-1,:-2])/4
        A = np.absolute(copym)-np.absolute(m)
        dif = np.amax(A)
        m = copym[:]
    pass
'''
def laplace (A,tol):
    """
    Use a docstring to explain what m and tol are.
    """

    dif = tol # This should be the tolerance parameter.
    
    copyA = A.copy()
    while dif >=tol:
        copyA[1:-1,1:-1]=(A[:-2,1:-1]+A[2:,1:-1]+
            A[1:-1,2:]+A[1:-1,:-2])/4.
        D = copyA - A
        dif = abs(np.max(D))
        A[:,:] = copyA[:,:]
    pass




def laplace_plot():    
    n = 100
    tol = .0001
    U = np.ones ((n, n))
    U[:,0] = 100 # sets north boundary condition
    U[:,-1] = 100 # sets south boundary condition
    U[0] = 0 # sets west boundary condition
    U[-1] = 0 # sets east boundary condition
    # U has been changed in place (note that laplace is the name of
    # the function in this case).
    laplace(U, tol)
    x = np.linspace(0, 1, n)
    y = np.linspace(0, 1, n)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.plot_surface (X, Y, U, rstride=5)
    plt.show()
    pass
#laplace_plot()

# Problem 5: Blue shift an RGB image

def blue_shift():
    A = np.random.randint(0,255,(100,100,3))
    tone_change = [.5, .5, 1.]
    changed = np.round(A * tone_change)
    return A, changed

def blue_shift_plot():
    original, blue = blue_shift()
    original = 255 - original
    blue = 255 - blue
    plt.subplot(1,2,1)
    plt.imshow(original)
    plt.subplot(1,2,2)
    plt.imshow(blue)
    plt.show()
    pass
blue_shift_plot()
