from scipy.linalg import svd, norm
import numpy as np

### Problem 1 ###
A = np.random.rand(5,5)

def svd_approx(A, k):
    if k == np.linalg.matrix_rank(A):
        return A
    else:
        U,s,Vt = svd(A, full_matrices = False)    
        rank = np.linalg.matrix_rank(A)
        cut = rank - k
        S = np.diag(s[:-cut])
        Ahat = U[:,:-cut].dot(S).dot(Vt[:-cut,:])
        return Ahat

print np.linalg.matrix_rank( svd_approx(A, 5))


### Problem 2 ### 

def lowest_rank_approx(A, e):
    """
    This is my function
    """
    error = 10
    k = 0
    Aold = A
    while error > e:
        k = k +1
        Anew = svd_approx(Aold, k)
        print error
        error = norm(Anew- Aold)
    return Anew, k

LowA, k = lowest_rank_approx(A,.8) 
print k


