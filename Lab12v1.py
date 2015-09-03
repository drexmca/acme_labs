import numpy as np
import math
from scipy.sparse import linalg as la
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from collections import Counter

### Problem 1 #### 


fatdata=np.loadtxt('weight_age_fat.txt',skiprows=1, usecols=(2,3,4))

fattitle=np.array(['weight','age','fat'])

def shiftByMean(array):
	means=np.mean(array, axis=0)
	newarray=array-means
	return newarray


print fatdata
print shiftByMean(fatdata)


def computeVariance(array):
	meanzeroarray=shiftByMean(array)
	sumsquare=np.sum(meanzeroarray**2,axis=0)
	n,m=np.shape(array)
	variance=sumsquare/n
	return variance

print computeVariance(fatdata)

def reportStDev(array, colname):
	var=computeVariance(array)
	sd=var**.5
	minsd=100
	name= 'none'
	for i in xrange(len(sd)):
		if minsd>sd[i]:
			name=colname[i]
			minsd=sd[i]

	print name, minsd

reportStDev(fatdata,fattitle)

### Problem 2 ### 

def corrMatrix(array):
    """
    Takes in the array, shifts it by the mean, takes the length, and
    finds the dotproduct to find the correlation, in a beautiful array
    """
    shiftarray=shiftByMean(array)
    normedarray=shiftarray/np.linalg.norm(shiftarray,axis=0)
    corr=np.dot(normedarray.T,normedarray)
    return corr

print corrMatrix(fatdata)

### Problem 3 ### 
mortality = np.loadtxt('mortality.txt', skiprows = 17)
mortalitydata = mortality [:, 1:]

def correlation(array):
    r2 = np.corrcoef(array, rowvar =0)
    n,m = np.shape(r2)
    for i in xrange(m):
        for j in xrange(n):
            if r2[i,j] ==1:
                r2[i,j]=0
    mcorr = 0
    col1 = 0 
    col2 =0
    for i in xrange(m):
        for j in xrange(n):
            if mcorr<r2[i,j]:
                mcorr = r2[i,j]
                col1=i
                col2 = j
    plt.subplot(1,3,1)
    plt.scatter(array[:,col1],array[:,col2])
    print ("Max correlation between the two columns: ", mcorr)

correlation(mortalitydata)


## Problem 4 ### 
print np.cov(mortalitydata, rowvar=0)
