
import numpy as np
import pylab
from scipy.integrate import quad
from matplotlib import pyplot as plt

#Problem3
def points(n):
    x = np.linspace(0,np.pi/2,n)
    return x
    
l = [10,30,100,300,1000]

for n in l:

    dx=(np.pi/2-0)/n

    x=np.linspace(0,np.pi/2,n)

    y=np.cos(x)

    SimpleMethod=y.sum()*dx

    print 'Integral is ' + repr(SimpleMethod) + ' and the number of points is ' + repr(n)


#Problem4
def SimpsonsRule(n):
    
    dx=np.pi/2/(n-1)*2
    
    y=np.cos(points(n))
      
    ye=y[2:-1:2]     #Select all even points from an array
    
    yo=y[1:-1:2]   #Select all odd points from an array
    
    tot=y[0]*1/6+np.sum(yo)*2/3+np.sum(ye)*1/3+y[-1]*1/6

    return tot*dx
    
if __name__=='__main__':

#Problem5
		Answer=SimpsonsRule(11)
  
		Error=np.abs(Answer-1)
  
		print 'Answer = ' + repr(Answer)
  
		print 'error on 11 points = ' + repr(Error)
  
l = [10,30,100,300,1000]

for n in l:
    
    Error=abs(SimpsonsRule(n)-1)
    
    print ' error for ' + repr(n) + ' points is ' + repr(Error)
    
#Question 6

l =[11,31,101,301,1001,3001,10001,3001,100001]  

l = np.array(l)

SimpsonError=np.zeros(l.size)

SimpleError=np.zeros(l.size)

for m in range(l.size):

    n=l[m]

    dx=np.pi/2/n

    x=np.linspace(0,np.pi/2,n)

    y=np.cos(x)

    SimpleMethod=y.sum()*dx

    SimpsonError[m]=np.abs(SimpsonsRule(n)-1)

    SimpleError[m]=np.abs(SimpleMethod-1)

    pylab.plot(l,SimpleError,'b-o')

    pylab.plot(l,SimpsonError,'r-o')

    ax=pylab.gca()

    ax.set_yscale('log')

    ax.set_xscale('log')
