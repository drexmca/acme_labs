# spec.py
import numpy as np
from matplotlib import pyplot as plt
import scipy.misc as sp
from numpy import linalg as la

# Problem 1: Implement this function.
def centered_difference_quotient(f,pts,h = 1e-5):
    '''
    Compute the centered difference quotient for function (f)
    given points (pts).
    Inputs:
        f (function): the function for which the derivative will be approximated
        pts (array): array of values to calculate the derivative
    Returns:
        centered difference quotient (array): array of the centered difference
            quotient
    '''
    diffs=np.zeros((len(pts)))
    dfapp= lambda x: .5*(f(x+h)-f(x-h))/h
    for i, p in enumerate(pts):
        diffs[i]=np.abs(sp.derivative(f,p)-dfapp(p))
    return diffs
   
# f = lambda x: np.exp(x)
# h=1e-1
# # Df_app = lambda x: .5*(f(x+h)-f(x-h))/h
# # print np.abs(f(1)-Df_app(1))
# # h = np.array([1e-1, 1e-3, 1e-5, 1e-7, 1e-9, 1e-11])
# pts=np.array([1,2,3])
# # Df_app = lambda x: .5*(f(x+h)-f(x-h))/h


# print centered_difference_quotient(f,pts,h)


# Problem 2: Implement this function.
def jacobian(f,n,m,pt,h = 1e-5):
    '''
    Compute the approximate Jacobian matrix of f at pt using the centered
    difference quotient.
    Inputs:
        f (function): the multidimensional function for which the derivative
            will be approximated
        n (int): dimension of the domain of f
        m (int): dimension of the range of f
        pt (array): an n-dimensional array representing a point in R^n
        h (float): a float to use in the centered difference approximation
    Returns:
        Jacobian matrix of f at pt using the centered difference quotient.
    '''
    identity=np.eye(n)
    return np.hstack([np.vstack(f(pt+ h*identity[i,:])-f(pt-h*identity[i,:]))/(2.0*h) for i in xrange(n)])




# Problem 3: Implement this function.
def findError():
    '''
    Compute the maximum error of your jacobian function for the function
    f(x,y)=[(e^x)*sin(y)+y^3,3y-cos(x)] on the square [-1,1]x[-1,1].
    Returns:
        Maximum error of your jacobian function.
    '''
    greatdiff = 0
    A= lambda x: np.array([[np.exp(x[0])*np.sin(x[1]), np.exp(x[0])*np.cos(x[1])+3*x[1]**2],[np.sin(x[0]), 3]])
    f= lambda x: np.array([np.exp(x[0])*np.sin(x[1])+ (x[1]**3),3*x[1]-np.cos(x[0])])
    x=np.linspace(-1,1,100)
    y=np.linspace(-1,1,100)
    for i in  x:
      for j in y:
        C=A([i,j])
        D=jacobian(f,2,2,[i,j])
        errormat = np.abs(C - D)
        if la.norm(errormat)> greatdiff:
          greatdiff=la.norm(errormat)
    return greatdiff

   
    
        
# Problem 4: Implement this function.
def Filter(image,F):
    '''
    Applies the filter to the image.
    Inputs:
        image (array): an array of the image
        F (array): an nxn filter to be applied (a numpy array).
    Returns:
        The filtered image.
    '''
    m, n = image.shape
    l, k = F.shape
    
    image_pad = np.zeros((n+l-1, n+k-1))
    image_pad[l/2:-(l/2), k/2:-(k/2)] = image
    
    C = np.empty_like(image)
    for i in xrange(n):
        for j in xrange(m):
            C[i, j] = np.sum(F * image_pad[i: i+l, j : j+k])
    return C


# Problem 5: Implement this function.
def sobelFilter(image):
    '''
    Applies the Sobel filter to the image
    Inputs:
        image(array): an array of the image in grayscale
    Returns:
        The image with the Sobel filter applied.
    '''
    S = 1. / 8 * np.array([[-1.,0.,1.],[-2.,0.,2.],[-1.,0.,1.]])
    image_x = Filter(image, S)
    image_y = Filter(image, S.T)
    maggradient = np.sqrt(image_x**2 + image_y**2)
    M = np.mean(maggradient) * 4
    return maggradient > M


# gausblur = 1. / 159 * np.array([[2.,  4.,  5.,  4.,  2.],
#                                    [4.,  9.,  12., 9.,  4.],
#                                    [5.,  12., 15., 12., 5.],
#                                    [4.,  9.,  12., 9.,  4.],
#                                    [2.,  4.,  5.,  4.,  2.]])
# img = plt.imread('cameraman.png')
# blur = Filter(img, gausblur)
# plt.imshow(blur, cmap='gray')
# plt.figure()
# plt.imshow(img, cmap='gray')
# plt.figure()
# plt.imshow(sobelFilter(blur), cmap='gray')
# plt.show()
    
