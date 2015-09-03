from __future__ import division
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.optimize as opt
import math
import pandas as pd
from numpy.matlib import repmat
from scipy import linalg as la
import math as math


##Problem 1##
def givens(A):
    R = np.copy(A)
    m,n = np.shape(A)
    Q = np.identity(len(A))
    G = np.zeros((2,2))
    for j in xrange(n):
        for i in xrange(m-1,j,-1):
            a,b = R[i-1, j], R[i,j]
            G = np.array([[a,b],[-b,a]])/(math.sqrt(a**2+b**2))
            R[i-1:i+1,j:]=np.dot(G,R[i-1:i+1,j:])
            Q[i-1:i+1,:] = np.dot(G,Q[i-1:i+1,:])
    return Q.T, R


## Problem 2 ##
 
def givens2(A):
    m,n = np.shape(A)
    R = A.astype(float)
    Q = np.eye(m)
    G = np.empty((2,2))
    for j in range(0, n-1):
        a= R[j, j]
        b= R[j+1,j]
        G = np.array([[a,b],[-b,a]])/la.norm([a,b])
        R[j:j+2, j:] = np.dot(G, R[j:j+2, j:])
        Q[j:j+2,:] = np.dot(G, Q[j:j+2, :])
    return np.transpose(Q), R

## Problem 3, 4 ##
def Least_squares(A,b):
    Q,R = la.qr(A)
    m,n = np.shape(R)
    R0 = R[:n,:n]
    right = np.dot(Q.T,b)
    right = right[:n,]
    x= la.solve_triangular(R0,right)
    return x
 
linepts = np.load('data.npz')['linepts']
linepts2 = np.zeros((197,3))
linepts2[:,0] = linepts[:,0]
linepts2[:,2] = linepts[:,1]
linepts2[:,1] = np.ones(197)
A = linepts2[:,0:2]
b = linepts2[:,2]
 
x = Least_squares(A,b)
print (x)
 
 
x0 = np.linspace(0,4000,4000)
y0 = x[0]*x0+x[1]
plt.plot(A[:,0],b,'*')
plt.plot(x0,y0)
plt.show()
 
### Problem 5 ###
 
 
circlepts = np.load('data.npz')['circlepts']
 
xsquared = np.zeros((200,1))
ysquared = np.zeros((200,1))
xy = np.zeros((200,1))
ones = np.ones((200,1))
 
for i in xrange(200):
    xsquared[i,0]=circlepts[i,0]*circlepts[i,0]
    ysquared[i,0]=circlepts[i,1]*circlepts[i,1]
    xy[i,0]=circlepts[i,0]*circlepts[i,1]
 
circlepts = np.append(circlepts,xsquared,1)
circlepts = np.append(circlepts,ysquared,1)
circlepts = np.append(circlepts,xy,1)
 
#print circlepts
 
circle_least_squares = Least_squares(circlepts,ones)
#x0 = np.linspace
 
print "a equals", circle_least_squares[2]
print "b equals", circle_least_squares[0]
print "c equals", circle_least_squares[4]
print "d equals", circle_least_squares[1]
print "e equals", circle_least_squares[3]
 
 
circlepts = np.load('data.npz')['circlepts']
 
A=np.hstack((2*circlepts,np.ones((len(circlepts),1))))
b = ((circlepts**2).sum(axis=1))
c1,c2,c3=Least_squares(A,b)
r=math.sqrt(c1**2+c2**2+c3)
theta = np.linspace(0,2*np.pi,200)
plt.plot(r*np.cos(theta)+c1,r*np.sin(theta)+c2,'-',circlepts[:,0],circlepts[:,1],'*')
plt.show()
