# spec.py
"""Volume I Lab 6: QR Decomposition.
Name:
Date:
"""

def QR(A):
    '''
    Compute the QR decomposition of a matrix.
    Accept an m by n matrix A of rank n. 
    Return Q, R
    '''
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
    
def prob2(A):
    '''
    Use your QR decomposition from the previous problem to compute 
    the determinant of A.
    Accept a square matrix A of full rank.
    Return |det(A)|.
    '''
    Q,R = QR(A)
    det = 1
    for i in xrange(len(R)):
        det = det*R[i,i]
    return det

def householder(A):
    '''
    Use the Householder algorithm to compute the QR decomposition
    of a matrix.
    Accept an m by n matrix A of rank n. 
    Return Q, R
    '''
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

def hessenberg(A):
    '''
    Compute the Hessenberg form of a matrix. Find orthogonal Q and upper
    Hessenberg H such that A = QtHQ.
    Accept a non-singular square matrix A.
    Return Q, H
    '''
    m,n = np.shape(A)
    H = np.copy(A)
    Q = np.identity(m)
    for k in range(n-2):
        uk = np.copy(H[k+1:, k])
        uk[0] = uk[0] + np.sign(uk[0])*la.norm(uk)
        uk = uk/la.norm(uk)
        H[k+1:, k:] = H[k+1:,k:] - 2*np.outer(uk, np.dot(uk.T, H[k+1:,k:]))
        H[:,k+1:] = H[:,k+1:] - 2*np.outer(np.dot(H[:,k+1:],uk), uk.T)
        Q[k+1:] = Q[k+1:] - 2*np.outer(uk.T, np.dot(uk.T, Q[k+1:]))
    return Q, H

def givens(A):
    '''
    EXTRA 20% CREDIT
    Compute the Givens triangularization of matrix A.
    Assume that at the ijth stage of the algorithm, a_ij will be nonzero.
    Accept A
    Return Q, R
    '''
    pass

def prob6(H):
    '''
    EXTRA 20% CREDIT
    Compute the Givens triangularization of an upper Hessenberg matrix.
    Accept upper Hessenberg H.
    
    '''
    pass
