import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math
import time
import decimal
import cymodule
 
 
#Exercise 1
np.set_printoptions(precision=30)
 
class float(object):
 
    def __init__(self,exponent=1,significant=10,number=0.0):
        self.exponent=exponent
        self.significant=significant
        self.float=number
 
    def convert(self,number):
        return number*self.significant**self.exponent
 
    def __repr__(self,number):
        newnumb=convert(self,number)
        return str(newnumb)
 
    def copy(self,number):
        return float(exponent=self.exponent,significant=self.significant, number=number)
 
    def __add__(self,other):
        if self.exponent != other.exponent:
            return "You are trying to break math!"
        if self.significant != other.significant:
            return "Nope, not gonna work"
        return float(exponent=self.exponent,significant=self.significant,number=self.number+other.number)
 
    def __mul__(self,other):
        if self.significant != other.significant:
            return "Nice Try!"
        return float(exponent=self.exponent+other.exponent,significant=self.significant,number=self.number*other.number)
 
    def __truncate__(self,digits):
        return float(exponent=self.exponent,significant=self.significant,number=round(self.round,digits))
 
class error(object):
 
    def __init__(self,exponent=1,significand=10,number=0.0,truenum=1,error=0):
        self.exponent=exponent
        self.significand=significand
        self.float=number
        self.truenum=truenum
        self.error=error
 
    def convert(self,number):
        error=abs(number*self.significand**self.exponent)-truenum
        self.error+=error
        return number*self.significand**self.exponent
 
    def __repr__(self,number):
        newnumb=convert(self,number)
        return str(newnumb)
 
    def copy(self,number):
        return Float(exponent=self.exponent,significand=self.significand,number=number,truenum=self.truenum,error=self.error)
 
    def __add__(self, other):
        if self.exponent != other.exponent:
            return "This is so dumb"
        if self.significand != other.significand:
            return "this is really dumb"
        newnum=convert(self.number+other.number)
        newerror=newnum-(self.truenum+other.truenum)
        return Float(exponent=self.exponent,significand=self.significand, \
        number=self.number+other.number,truenum=self.truenum+other.truenum, \
        error=newerror)
 
    def __sub__(self,other):
        if self.exponent != other.exponent:
            return "Ha ha!"
        if self.significand != other.significand:
            return "Your mom is a jail bird!"
        newnum=convert(self.number-other.number)
        newerror=newnum-(self.truenum-other.truenum)
        return Float(exponent=self.exponent,significand=self.significand,number=self.number-other.number,truenum=self.truenum-other.truenum,error=newerror)
 
    def __mul__(self, other):
        if self.significand != other.significand:
            return "this is really dumb"
        newnum=Float(exponent=self.exponent+other.exponent,significand=\
        self.significand, number=self.number*other.number,truenum=self.truenum*other.truenum, error=0)
        newerror=convert(newnum)-(self.truenum*other.truenum)
        return Float(exponent=self.exponent+other.exponent,significand=\
        self.significand, number=self.number*other.number,truenum=\
        self.truenum*other.truenum, error=newerror)
  
    def truncate(self):
        i=-20
        while 10**i <=self.error:
            num=10**i
            i+=1
        return Float(exponent=self.exponent,significand=self.significand, \
        number=round(number,i-1), truenum=self.truenum,error=self.error)
 
 
def pysqrt64(A,reps):
    Ac=A.copy()
    I=Ac.view(dtype=np.int64)
    I >>=1
    I += (1<<61)-(1<<51)
    for i in xrange(reps):
        Ac=.5*(Ac+A/Ac)
 
    return Ac
 
a=np.array([1234.])
print pysqrt64(a,10)
 
start=time.time()
pysqrt64(a,10)
Timer1=time.time()-start
print "Custom Function time:", Timer1
start=time.time()
np.sqrt(a)
Timer2=time.time()-start
print "Numpy Function Time:",Timer2
start=time.time()
cymodule.pysqrt64(a,10)
Timer3=time.time()-start
print "Cython Time:",Timer3
