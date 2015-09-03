import numpy as np
from matplotlib import pyplot as plt
from math import sqrt


### Problem 1 ###
def f(x):
    return x*x


def G(x):
    return (9./8.)*x**3.+(45./8.)*x**2+(75./8.)*x

print (G(1)-G(-1))


def gauss(f, x, b, a):
    return (((b-a)/2.)*f(((b-a)/2.)*x+(b+a)/2.))

x1 = np.linspace(1,4,200)
x2 = np.linspace(-1,1,200)
y1 = f(x1)
y2 = gauss(f,x2, 4., 1.)
plt.subplot(1,2,1)
plt.title('f(x)')
plt.plot(x1, y1)
plt.subplot(1,2,2)
plt.title('g(x)')
plt.plot(x2, y2)
plt.show()

### Problem 2 ###

def func2(func, points, weights, lim1, lim2):
    
    g1 = lambda x: func((lim2-lim1)/ 2 * x + (lim1 + lim2) / 2)
    return (lim2-lim1)/2 * np.inner(weights, g1(points))

a, b = -np.pi, np.pi
func = np.sin
points = np.array([- sqrt(5 + 2 * sqrt(10. / 7)) / 3,
                   - sqrt(5 - 2 * sqrt(10. / 7)) / 3,
                   0,
                   sqrt(5 - 2 * sqrt(10. / 7)) / 3,
                   sqrt(5 + 2 * sqrt(10. / 7)) / 3])
weights = np.array([(322 - 13 * sqrt(70)) / 900,
                    (322 + 13 * sqrt(70)) / 900,
                    128. / 225,
                    (322 + 13 * sqrt(70)) / 900,
                    (322 - 13 * sqrt(70)) / 900])


integral = (b - a)/2 * np.inner(weights, gauss(func, points,a,b ))

integraltest = func2(func, points, weights, a, b)
print integral
print integraltest


### Problem 3 ## 


def jacob(alpha, beta, gamma):
    a = -beta/alpha
    b = (gamma[1:]/(alpha[:-1]*alpha[1:]))**0.5
    jacobian = np.diag(b,-1) + np.diag(a,0) + np.diag(b,1) 
    return jacobian

### Problem 4 ###




