import numpy as np
import scipy.misc as sp
from matplotlib import pyplot as plt


## Problem 1
f = lambda x: np.exp(x)

pts =np.array([1,2,3])

def cent_dq(f, pts, h = (1e-5)):
    Df_app = lambda x: .5*(f(x+h)-f(x-h))/h
    d = np.zeros((len(pts)))
    for i, p in enumerate(pts):
        d[i] = np.abs(Df_app(p)-sp.derivative(f, p))
    return d

print cent_dq(f, pts)

## Problem 2
## part 1:
def approx_jacobian(f, m, n, pt, h = (1e-5)):
    Df_app = lambda x, f, e: .5*(f(x+h*e) - f(x-h*e))/h
    identity = np.identity(n)
    jacobian = np.zeros((m, n))
    for i in range(n):
        e = identity[:][i]
        jacobian[:][i] = Df_app(pt, f, e)
    return jacobian.T

def fxy(pt):
    return np.array((pt[0]**2)*pt[1], (pt[1]**2)*pt[0])

pt = np.array([2,2])

Jacobian1 = approx_jacobian(fxy, 2, 2, pt)
print Jacobian1

## part 2:
def norm(A, B):
    d = np.abs(A - B)
    d = np.reshape(d, (4))
    norm = np.dot(d, d)
    return norm

func = lambda x: np.array([np.exp(x[0])*np.sin(x[1]) + x[1]**3, 3*x[1] - np.cos(x[0])])

x = np.linspace(-1,1,100)
y = np.linspace(-1,1,100)

A = lambda x: np.array([[np.exp(x[0])*np.sin(x[1]), np.exp(x[0])*np.cos(x[1]) + 3*x[1]**2],[np.sin(x[0]), 3]])

max_norm = 0

for i in x:
    for j in y:
        C = A([i, j])
        D = approx_jacobian(func, 2, 2, [i, j])
        if norm(C, D) > max_norm:
            max_norm = norm(C, D)
print max_norm  

## Problem 3:


def Filter(image, filter):
    m, n = image.shape
    h, k = filter.shape
    
    image_pad = np.zeros((m + h - 1, n + k - 1))
    image_pad[h/2 : -(h/2) , (k/2) : -(k/2)] = image
    
    C = np.empty_like(image)
    for i in xrange(n):
         for j in xrange(m):
             C[i, j] = np.sum(filter * image_pad[i:i+h, j:j+k])
    return C

## Problem 4:
G =  np.array([[2.,  4.,  5.,  4.,  2.],
               [4.,  9.,  12., 9.,  4.],
               [5.,  12., 15., 12., 5.],
               [4.,  9.,  12., 9.,  4.],
               [2.,  4.,  5.,  4.,  2.]])

G = (1./159) * G

S =  np.array([[-1.,0.,1.],[-2.,0.,2.],[-1.,0.,1.]])
S = (1./8) * S

def sobel(image):
    image1 = Filter(image, S)
    image2 = Filter(image, S.T)
    grad = np.sqrt(image1**2 + image2**2  )
    mean = np.mean(grad) * 4
    return grad > mean

fig = plt.imread('cameraman.png')
blurred = Filter(fig, G)
plt.imshow(blurred, cmap='gray')
plt.figure()
plt.imshow(fig, cmap='gray')
plt.figure()
plt.imshow(sobel(blurred), cmap='gray')
plt.show()
