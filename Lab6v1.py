#Problem 1
import numpy as np
from matplotlib import pyplot as plt
import scipy as sp

x123=[10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
y1=[8.04,6.95,7.58,8.81,8.33,9.96,7.24,.26,10.84,4.82,5.68]
y2=[9.14,8.14,8.74,8.77,9.26,8.1,6.13,3.1,9.13,7.26,4.74]
y3=[7.46,6.77,12.74,7.11,1.81,8.84,6.08,5.39,8.15,6.42,5.73]
x4=[8.,8.,8.,8.,8.,8.,8.,19.,8.,8.,8.]
y4=[6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.5,5.56,7.91,6.89]

plt.subplot(411)
plt.scatter(x123,y1)
plt.subplot(412)
plt.scatter(x123,y2)
plt.subplot(413)
plt.scatter(x123,y3)
plt.subplot(414)
plt.scatter(x4, y4)
plt.show()

#Note that they all look different, even though they all have the same statistics
# You didn't really do the stuff to simplify the graph.  It's really useful 
# for making professional graphs fro presentations and papers.
x = np.linspace(0,5,250)
y = np.linspace(0,5,250)
X, Y = np.meshgrid(x,y)

func = np.absolute((X+Y*1.0j)**3+2*(X+Y*1.0j)**2-(X+Y*1.0j)+3)
plt.pcolormesh(X,Y,func, cmap="gray")
plt.xticks(np.arange(0,5,.5))
plt.yticks(np.arange(0,5,.5))

plt.show()


