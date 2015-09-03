import numpy as np
from scipy import linalg as la
from matplotlib import pyplot as plt



def Plot(old, new):
    """
    Takes in two data sets, and plots them in the same window. Currently, it is 
    auto-adjusting the axes, which produces funky results in a lab that is 
    focused on showing changes in the data sets. Figure out a way to keep the 
    axes fixed where you want?
    """

    #plt.autoscale(enable = False)
    plt.subplot(2,1,1)
    plt.scatter(old[0], old[1])
    plt.axis('equal')
    plt.subplot(2,1,2)
    plt.scatter(new[0], new[1])
    plt.axis('equal')
    plt.show()

with np.load('data.npz') as data:
    circle = data['circlepts']
circle = circle.T
circle = np.array(circle)

## Problem 1 ##
def stretcher(circle, stretch):
    """
    This function takes in a data set, and a scaler value to stretch the data set
    by, and then plots them using the above defined Plot function.
    """
    k = np.zeros(2) + stretch
    dilate = np.diag(k)
    return dilate.dot(circle)


## Problem 2 ## 
def rotate(circle, theta):
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
    return rmatrix.dot(circle)


## Problem 3 ##
def shear(data, k, dirct):
    """
    Takes in a data set, plots a new function with either a vertical, or 
    horizantal shear applied. 
    ## Paramaters ## 
    data: 2xn array to plot
    k: the shear factor
    dirct: direction you want to shear. 0 for horizontal, 1 for vertical
    """
    smatrix=np.identity(2)
    if dirct ==0:
        smatrix[0][1] =k 
    else:
        smatrix[1][0] = k
    print smatrix
    return smatrix.dot(data)

    
## Problm 4 ##
def householder(data, l):
    """
    Takes a data set, returns a new with a householder reflection.
    ## paramaters ##
    l: a 2 element 1-D array that has the span of the vector you want to rotate
    around
    data: your data set, dummy.
    """
    hmatrix = np.identity(2)
    hmatrix[0][0] = l[0]**2-l[1]**2
    hmatrix[0][1] = 2*l[0]*l[1]
    hmatrix[1][0] = 2*l[0]*l[1]
    hmatrix[1][1] = l[1]**2-l[0]**2
    hmatrix = (1./(l[0]**2+l[1]**2))*hmatrix
    return hmatrix.dot(data)

## Problem 5 ##
def translation(data, shift):
    """z
    This function shifts your original data set.
    ## Parameters ##
    trans: a 2 element array that tells how much to shift the x and y
    data: your data
    """
    newdata = np.copy(data)
    #newdata[0][:] = newdata[0][:] + trans[0]
    #newdata[1][:] = newdata[1][:] + trans[1]
    shift = np.array([[shift[0], shift[1]]])
    
    return newdata + shift

slide = [[200],[0]]
#Plot(circle, translation(circle, slide))

## Problem 6 ##


def rotation(t, w, v, s):
    p1 = np.array([1,0])
    p2 = np.array([0,0])
    p2 = np.multiply(v, ((s*t)/(np.linalg.norm(v))))
    p1 = rotate(p1, t*w)
    p1= translation(p1, p2)
    return p1



t= np.linspace(0.1, 10, 100)
pos = np.zeros((2,len(t)))
for i in xrange(len(t)):
    pos[:,i]=rotation(t[i],np.pi, [1,1], 3).flatten()
plt.plot(pos[0], pos[1])
# plt.show()

## Problem 7 ## 

rowmatrix = np.array([[7,4,6],[3,2,8],[5,3,2]])
print (type(rowmatrix))


def rowreduce(A):
    for i in xrange(len(A)-1):
        A[i,:]=A[i,:]/A[i,i]
        for j in xrange(i,len(A)-1):
            A[i+1,:]=A[i+1,:]-(A[i+1,i]*A[i,:])
        A[-1, :] = A[-1,:]-(A[-1,i]*A[i,:])
        A[-1,-1]=1.


rowreduce(rowmatrix)

## Problem 8 ##

rowmatrix = np.array([[7,4,6],[3,2,8],[5,3,2]])

def ludecomp(A):
    U = np.copy(A)
    L = np.identity(len(A))
    for j in xrange(len(A)):
        for i in xrange (len(A)):
            L[i,j]=U[i,j]/U[j,j]
            U[i,j:] = U[i,j:]-L[i,j]*U[j,j:]
    return L, U


L, U =ludecomp(rowmatrix)
print (L, U)

## Problem 10 ## 
"""
1. timed using ipython, 125 ms per loop.
2. timed using ipython, 388 ms per loop.
"""
A = np.random.random((1000,1000))
B = np.random.random((1000,500))

Ainv = la.inv(A)
AU=la.lu_factor(A)
la.lu_solve(AU,B)
#This one took 183 ms per loop

Ainv.np.dot(B)
#This took 160 ms per loop

#Always better to not take the inverse






