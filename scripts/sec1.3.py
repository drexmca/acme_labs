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
def Prob17():
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
        print 'For A(BX), and k = {}, time = {}, ratio = {}'.format(k, b,
                (a/b))

#Prob17()
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
def Prob18():

    for k in xrange(1,5):
        I = np.eye(10**k)
        u = np.random.rand(10**k)
        v = np.random.rand(10**k)
        x = np.random.rand(10**k)
        start = time.time()
        np.dot(I+np.dot(u,v.T),x)
        a = time.time()-start
        start = time.time()
        x+np.dot(np.dot(v.T,x),u)
        b = time.time() - start
        print 'For Method 1, and k = {}, time = {}'.format(k, a)
        print 'For Method 2, and k = {}, time = {}'.format(k, b)
        print 'Difference = {}'.format(a-b)
        print 'Ratio of Method 1 to Method 2 = {}'.format(a/b)
Prob18()
'''
1
For Method 1, and k = 1, time = 4.31537628174e-05
For Method 2, and k = 1, time = 4.05311584473e-06
Difference = 3.88622283936e-05
Ratio of Method 1 to Method 2 = 10.6470588235

2
For Method 1, and k = 2, time = 3.69548797607e-05
For Method 2, and k = 2, time = 3.09944152832e-06
Difference = 3.38559224924e-05
Ratio of Method 1 to Method 2 = 11.9230769231

3
For Method 1, and k = 3, time = 0.00465798377991
For Method 2, and k = 3, time = 1.90734863281e-05
Difference = 0.00457000732422
Ratio of Method 1 to Method 2 = 244.2125

4
For Method 1, and k = 4, time = 0.530934095383
For Method 2, and k = 4, time = 0.000128984451294
Difference = 0.538677930832
Ratio of Method 1 to Method 2 = 4116.26432532
'''



