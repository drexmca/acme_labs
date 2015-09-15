# name this file 'solutions.py'
"""Volume I Lab 3: Plotting with matplotlib
Donald Rex McArthur
Sept. 14, 2015
"""

# Add your import statements here.
from mayavi import mlab 
from matplotlib import pyplot as plt
import numpy as np

# Problem 1
def curve():
    """Plot the curve 1/(x-1) on [-2,6]. Plot the two sides of the curve separately
    (still with a single call to plt.plot()) so that the graph looks discontinuous 
    at x = 1.
    """
    x=np.linspace(-2,6,1000)
    y=1/(x-1)
    a=100
    b=-a
    y[y>a]= np.inf
    y[y<b] = -np.inf
    x1,x2,y1,y2 = plt.axis()
    plt.axis((-2,6,-6,6))
    
    plt.plot(x,y,'--m', linewidth = 5)
    plt.show()
    pass

# Problem 2
def colormesh():
    """Plot the function f(x,y) = sin(x)sin(y)/(xy) on [-2*pi, 2*pi]x[-2*pi, 2*pi].
    Include the scale bar in your plot.
    """
    x = np.linspace(-2*np.pi,2*np.pi,250)
    y = np.linspace(-2*np.pi,2*np.pi,250)
    X, Y = np.meshgrid(x,y)
    
    func = (np.sin(X)*np.sin(Y))/(X*Y)
    plt.axis([-2*np.pi, 2*np.pi,-2*np.pi,2*np.pi])
    plt.pcolormesh(X,Y,func, cmap='seismic')
    plt.colorbar()
    plt.gca().set_aspect('equal')
    plt.show()
    pass

# Problem 3
def histogram():
    """Plot a histogram and a scatter plot of 50 random numbers chosen in the
    interval [0,1).
    """
    x = np.linspace(1,50,50)
    y1 = np.random.rand(50)
    
    plt.subplot(122)
    mean = np.mean(y1)
    mean_line = np.linspace(mean,mean,50)
    plt.plot(x, mean_line)
    plt.scatter(x,y1)
    plt.axis([0,50,0,1])
    plt.title('50 randy dots')
    
    plt.subplot(121)
    plt.hist(y1, bins=5, range =[0,1])
    plt.title('50 randy histos')
    
    
    plt.suptitle("My different plots")
    
    plt.show()
    pass
    
# Problem 4
def ripple():
    """Plot z = sin(10(x^2 + y^2))/10 on [-1,1]x[-1,1] using Mayavi."""
    X, Y = np.mgrid[-1:1:.01, -1:1:0.01]
    Z = np.sin(10*(X**2+Y**2))/10
    mlab.surf(X,Y,Z, colormap='RdYlGn') 
    mlab.show()
    pass

curve()
colormesh()
histogram()
ripple()
