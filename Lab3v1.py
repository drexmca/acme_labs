from mayavi import mlab # All of the imports are at the top.  That's good.
from matplotlib import pyplot as plt
import numpy as np

"""
The only important thing in this lab was getting the plots.  Matplotlib is messy
I didn't expect your first encounter with it to be clean.
"""

x=np.linspace(0,2*np.pi,157)
y=[np.sin(x),np.cos(x)]
plt.plot(x,y[0],'r:', x, y[1], 'b:')
plt.show()


x=np.linspace(-2,6,1342)
y=1/(x-1)
a=100
b=-a
y[y>a]=np.inf
y[y<b] = -np.inf
x1,x2,y1,y2 = plt.axis()
plt.axis((-2,6,-6,6))

plt.plot(x,y,'--m', linewidth = 5)
plt.show()

z=np.linspace(0,10,340)
g = (np.sin(z))/(z+1)
#print (g)
zh=g.clip(0)
zg=g.clip(max=0)
plt.plot(z,zg,z,zh,)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.fill_between(z,0,zg, color = 'b')
plt.fill_between(z,0,zh, color = 'r')
maxval = []
plt.grid(b=True)
for i in range (1,len(z)-1): # I like how you did this.
    d1=g[i]-g[i-1]
    d2=g[i+1]-g[i]
    if np.sign(d1) != np.sign(d2):
        maxval.append(i)
for x in maxval:
    plt.plot(z[x], .5*g[x], 'k^')

plt.show()


#Problem 4
x = np.linspace(0,2,250)
y = np.linspace(0,2,250)
X, Y = np.meshgrid(x,y)

func = np.absolute((X+Y*1.0j)**3+2*(X+Y*1.0j)**2-(X+Y*1.0j)+3)
plt.pcolormesh(X,Y,func)
plt.show()


#Problem 5

x= np.linspace(-np.pi,np.pi,400)
ysin=np.sin(x)
ycos=np.cos(x)
ysquared = x**2
ye=np.exp(x)
plt.subplot(411)
plt.plot(x,ysin)
plt.title('Sin(x)')

plt.subplot(412)
plt.plot(x,ycos)
plt.title('Cos(x)')

plt.subplot(413)
plt.plot(x, ye)
plt.title('e^(x)')

plt.subplot(414)
plt.plot(x, ysquared)
plt.title('x^(2)')

plt.suptitle("My different plots")

plt.show()

# Problem 6
# This filepath only works on your computer.  Anytime your code 
# relies on a file you need to include it in the repo.  Absolute
# filepaths are great, but they are bound to one machine.
GrandCanyon = np.load("/home/drexmca/repos/Shared/GrandCanyon.npy") 
GrandCanyon=np.reshape(GrandCanyon,[3601,3601])
GrandCanyon = GrandCanyon.astype(np.float32, copy = False)
GrandCanyon=GrandCanyon[:999,899:1899]
positivegrand=np.absolute(GrandCanyon)
print(positivegrand)
minval=np.min(positivegrand)
print (minval)
print(np.min(GrandCanyon))

GrandCanyon=GrandCanyon.clip(min=minval)
print(np.min(GrandCanyon))
mlab.figure(size=(400,320),bgcolor = (.16, .28, .46))
mlab.surf(GrandCanyon, colormap="gist_earth", warp_scale=.2, vmin=1200, vmax=1610)
mlab.view(-5.9,83,570,[5.3,20,238])
mlab.show()

