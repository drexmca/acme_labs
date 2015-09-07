'''
Sec 1.3
Math 320 
Donald Rex McArthur
Sept. 7, 2015
'''
import numpy as np
import time

## Problem 14 part 1
L = [3, 6, 2, 5, 9, 72, 0, 1]
def find_min_index(L):
    min_index = 0
    for i in xrange(len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

L = [3, 6, 2, 5, 9, 72, 0, 1, 43, 59, -8, 0]
print find_min_index(L)
# Returns 10 as expected
# The Best and Worst case scenarios here are identical because
# one must go through the whole list, so it is O(n).
# For spatial complexit, the best is 1, since you could get the min value
# in the first element, but the worst is it has to be written n times.


## Problem 1.15
def selection_sort(L):
    for i in xrange(len(L)-1):
        a = find_min_index(L[i:])
        if L[i] != L[a+i]:
            L[i], L[a+i]  = L[a+i], L[i]
    return L

print selection_sort(L)
# Prints the sorted list correctly.


def distance(x, y):
    return (abs(x[0]-y[0]) + abs(x[1]-y[1]))

## Problem 1.16
def brute_force(L):
    min_d = np.inf
    m_dim = [0,0]
    m,n = L.shape
    for i in xrange(m):
        for j in xrange(i+1,m):
            d = distance(L[i,], L[j,])
            if d < min_d:
                min_d = d
                m_dim = [i, j]
    close_points = L[m_dim[0],], L[m_dim[1],]
    return close_points
pts = np.array(([13,25], [43,-35], [1,6], [1,94], [2,6]))
close_pt = brute_force(pts)
print close_pt
# Prints [1,6], [2,6] as expected

## Problem 1.17

for k in xrange(1,5):
    print k
    A = np.random.rand(10**k,10**k)
    B = np.random.rand(10**k,10**k)
    X = np.random.rand(10**k,1)
    start = time.time()
    np.dot(np.dot(A,B),X)
    a = time.time()-start
    print 'For (AB)X, and k = {}, time = {}'.format(k, a)
    start = time.time()
    np.dot(A, np.dot(B,X))
    b = time.time()-start
    print 'For A(BX), and k = {}, time = {}, ratio = {}'.format(k, b, (a/b))

'''
1
For (AB)X, and k = 1, time = 4.91142272949e-05
For A(BX), and k = 1, time = 2.14576721191e-06, ratio = 22.8888888889
2
For (AB)X, and k = 2, time = 0.000133037567139
For A(BX), and k = 2, time = 7.86781311035e-06, ratio = 16.9090909091
3
For (AB)X, and k = 3, time = 0.0181860923767
For A(BX), and k = 3, time = 0.000968933105469, ratio = 18.7691929134
4
For (AB)X, and k = 4, time = 14.3529160023
For A(BX), and k = 4, time = 0.0754389762878, ratio = 190.258626357
'''

