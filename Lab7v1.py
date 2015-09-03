import numpy as np
from scipy import linalg as la

### Problem 1 ###

def QR(A):
    m,n = np.shape(A) 
    Q = np.copy(A)
    QT = Q.T
    R = np.zeros((n,n))
    for i in xrange(n):
        R[i,i] = np.linalg.norm(Q[:,i])
        Q[:,i] = Q[:,i]/R[i,i]
        for j in xrange(i+1,n): 
            R[i,j]= np.inner(Q[:,j],Q[:,i])
            Q[:,j]=Q[:,j]-R[i,j]*Q[:,i]
    return Q,R

A =np.array( [[1,1,0],[1,0,1],[0,1,1]])
A = A*1.
Q, R = QR(A)

### Problem 2 ###
def compdeter(A):
    Q,R = QR(A)
    det = 1
    for i in xrange(len(R)):
        det = det*R[i,i]
    return det

print compdeter(A)

## Problem 3 ##
def householder(A):
    (m,n) = np.shape(A)
    R = np.copy(A)
    Q = np.identity(m)
    for k in range(n-1):
        uk = np.copy(R[k:,k])
        uk[0] = uk[0]+(np.sign(uk[0])*np.linalg.norm(uk))
        uk = uk/np.linalg.norm(uk)
        R[k:,k:] = R[k:,k:] - 2*np.outer(uk, np.dot(uk.T, R[k:,k:]))
        Q[k:] = Q[k:] - 2*np.outer(uk, np.dot(uk.T, Q[k:]))
    QH = Q.T.conjugate()
    return QH, R

Q, R = householder(A)
print np.dot(Q,R)

print householder(A)

def hessenberg(A):
    m,n = np.shape(A)
    H = np.copy(A)
    Q = np.identity(m)
    for k in range(n-2):
        uk = np.copy(H[k+1:, k])
        uk[0] = uk[0] + np.sign(uk[0])*linalg.norm(uk)
        uk = uk/linalg.norm(uk)
        H[k+1:, k:] = H[k+1:,k:] - 2*np.outer(uk, np.dot(uk.T, H[k+1:,k:]))
        H[:,k+1:] = H[:,k+1:] - 2*np.outer(np.dot(H[:,k+1:],uk), uk.T)
        Q[k+1:] = Q[k+1:] - 2*np.outer(uk.T, np.dot(uk.T, Q[k+1:]))
    return Q, H

Q,H = hessenberg(A)
print np.dot(Q.T, np.dot(H,Q))


