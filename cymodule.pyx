from __future__ import division
import numpy as np
cimport numpy as np
cimport cython

def cypysum(x):
    cdef float summ = 0
    cdef int i,n  = 0
    n = len(x)
    for i in xrange(n):
        summ = summ + x[i]

def cysum_p(x):
    total = 0
    for i in range(0, len(x)):
        total += x[i]
    return total


def pymatpow(X, power):
    prod = X.copy()
    temparr = np.empty_like(X[0])
    size = X.shape[0]
    for n in xrange(1,power):
        for i in xrange(size):
            for j in xrange(size):
                tot = 0.
                for k in xrange(size):
                    tot += prod[i,k] * X[k,j]
                temparr[j] = tot
            prod[i] = temparr
    return prod



def pytridiag(a, b, c, x):
        n = x.size
        temp = 0.
        c[0] /= b[0]
        x[0] /= b[0]
        for i in xrange(n-2):
            temp = 1. / (b[i+1] - a[i] * c[i])
            c[i+1] *= temp
            x[i+1] = (x[i+1] - a[i] * x[i]) * temp
        x[n-1] = (x[n-1] - a[n-2] * x[n-2]) / (b[n-1] - a[n-2] * c[n-2])
        for i in xrange(n-2, -1, -1):
            x[i] = x[i] - c[i] * x[i+1]


