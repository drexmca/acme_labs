# solutions.py
from scipy import linalg as la
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from matplotlib import cm
from copy import copy

# Problem 1
def truncated_svd(A,r=None,tol=10**-6):
    """Computes the truncated SVD of A. If r is None or equals the number 
        of nonzero singular values, it is the compact SVD.
    Parameters:
        A: the matrix
        r: the number of singular values to use
        tol: the tolerance for zero
    Returns:
        U - the matrix U in the SVD
        s - the diagonals of Sigma in the SVD
        Vh - the matrix V^H in the SVD
    """
    m, n = A.shape
    AHA = np.dot(A.conj().T, A)
    values, vectors = la.eig(AHA)
    if r == None:
        r = 0
        for val in values:
            if not np.isclose(val, 0):
                r+=1

    vectors = vectors.T
    sorted_indices = np.argsort(values)
    sorted_indices = sorted_indices[::-1]
    sorted_values = np.zeros(len(values))
    sorted_vectors = np.zeros((vectors.shape))
    for i, index in enumerate(sorted_indices):
        sorted_values[i] = values[index]
        sorted_vectors[i] = vectors[i]

    sorted_values = sorted_values[:r]
    sorted_vectors = sorted_vectors[:r]

    singular_values = np.sqrt(sorted_values)
    s = np.diagflat(singular_values)
    
    U = np.zeros((m,r))
    for i, vector in enumerate(sorted_vectors):
        U[:,i] = 1./singular_values[i] * np.dot(A, vector.T)

    Vh = sorted_vectors.conj()

    return U, s, Vh

def test1():
    A = np.array([[2,5,4],[6,3,0],[6,3,0],[2,5,4]])
    print truncated_svd(A, r=1)[0]
    print truncated_svd(A)[1]
    print truncated_svd(A)[2]

#test1()


# Problem 2
def visualize_svd():
    """Plot each transformation associated with the SVD of A."""
    A = np.array([[3,1],[1,3]])
    U, s , Vh = truncated_svd(A)
    
    circle_pts = np.load('circle.npz')['circle']
    Vh_circle_pts = np.dot(Vh, circle_pts)
    s_circle_pts = np.dot(s, np.dot(Vh, circle_pts))
    U_circle_pts = np.dot(U, np.dot(s, np.dot(Vh, circle_pts)))
    
    unit_vecs = np.load('circle.npz')['unit_vectors']
    Vh_unit_vecs = np.dot(Vh, unit_vecs)
    s_unit_vecs = np.dot(s, np.dot(Vh, unit_vecs))
    U_unit_vecs = np.dot(U, np.dot(s, np.dot(Vh, unit_vecs)))
    
    data = [(circle_pts, unit_vecs), (Vh_circle_pts, Vh_unit_vecs), (s_circle_pts, s_unit_vecs), (U_circle_pts, U_unit_vecs)]

    for j, pair in enumerate(data):
        x = []
        y = []
    
        for i, x_pt in enumerate(pair[0][0]):
            x.append(x_pt)
            y.append(pair[0][1][i])
    
        plt.subplot(2, 2, j+1)
        plt.plot(x, y)
        plt.plot(pair[1][0], pair[1][1])
    
    plt.show()
 
#visualize_svd()

# Problem 3
def svd_approx(A, k):
    """Returns best rank k approximation to A with respect to the induced 2-norm.
    
    Inputs:
    A - np.ndarray of size mxn
    k - rank 
    
    Return:
    Ahat - the best rank k approximation
    """
    U,s,Vh = la.svd(A, full_matrices=False)
    rank = len(s)
    print s
    d = rank - k
    S = np.diag(s[:k])
    Ahat = U[:,:k].dot(S).dot(Vh[:k,:])
    
    return Ahat 
def test3():
    A = np.array([[1,1,3,4], [5,4,3,7], [9,10,10,12], [13,14,15,16], [17,18,19,20]])
    svd_approx(A, 3)

#test3()

# Problem 4
def lowest_rank_approx(A,e):
    """Returns the lowest rank approximation of A with error less than e 
    with respect to the induced 2-norm.
    
    Inputs:
    A - np.ndarray of size mxn
    e - error
    
    Return:
    Ahat - the lowest rank approximation of A with error less than e.
    """
    U,singular,Vh = la.svd(A, full_matrices=False)
    s=0
    while singular[s] > e:
        s+=1
    print s
    return svd_approx(A, s-1)
        
def test4():
    A = np.array([[1,1,3,4], [5,4,3,7], [9,10,10,12], [13,14,15,16], [17,18,19,20]])
    print lowest_rank_approx(A, 2.0) 
    print lowest_rank_approx(A, 2.5) 
#test4()
     
# Problem 5
def compress_image(filename,k):
    """Plot the original image found at 'filename' and the rank k approximation
    of the image found at 'filename.'
    
    filename - jpg image file path
    k - rank
    """
    im1 = mpimg.imread(filename)
    im2 = copy(im1)
    
    for i in xrange(2):
        im2[:,:,i] = svd_approx(im1[:,:,i], k)
    
    plt.subplot(121)
    plt.imshow(im1)
    plt.title("Original Image")
    plt.subplot(122)
    plt.imshow(im2)
    plt.title("Best Rank {} Approximation".format(k))
    plt.show()

#compress_image('hubble_image.jpg', 20)
