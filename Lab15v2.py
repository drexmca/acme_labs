import numpy as np
#import cymodule
import matplotlib.pyplot as plt
import scipy as sp
import math
import timeit
import time
 
### Exercise 1 ###
 
"""
There is such a large error because the numbers you are dealing with are 
single floats. If you used doubles, you could accurately reprsent a larger
number.
"""
 
### Exercise 2 ###
 
h=np.linspace(.0000000000001,.000000000001,1000)
x=np.linspace(-5,5,1000)
y=abs((np.sin(1+h)-np.sin(1))/h-np.cos(1))
plt.plot(h,y)
plt.show()
 




### Exercise 3 ###
 
 
def lnapprox(x,n=3):
    summed = 0
     
    for m in xrange(n+1):
        equa=((-1)**m*x**m)/(m+1)
        summed = summed + equa
### Apparently, this one is wrong. I got this one from Joe. Thanks joe. 
    return summed
 
x1=np.linspace(-5,30,1000)
x2=np.linspace(1,30,1000)
x2new=10**(-x2)
y1=np.log(10**(-x1)+1)*10**(x1)
y2=lnapprox(x2new)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.ylim(0,2)
plt.show()
 
#Exercise 4

''' 
Basically the same as Exercise 1. I wouldn't trust this large of float
approximations with a bag of beans.
'''
 
#Exercise 5
 
calcerror = .1-(209715./2097152.)
total_error = calcerror*100.*1676.*60.*60.
print total_error 
