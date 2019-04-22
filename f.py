#!/usr/bin/env python 
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from dist import dist
from one_step import isOneReach

#fig=plt.figure()
#ax=plt.axes(projection='3d')
a=np.ones((2,3,4),dtype=np.float)
#np.savetxt("foo.csv",a,delimiter=",")
#with open('outfile.txt','wb') as f:
 #   for line in a:
  #      np.savetxt(f,line,fmt='%.2f')
x=range(0,40)
y=range(0,40)
X,Y=np.meshgrid(x,y)
input=np.loadtxt("outfile.txt",dtype=np.float)
a=input.reshape(40,40)
#print a
#V=np.zeros((40,40),dtype=np.int)
#V[10,15]=1
#V[20,35]=1
fig, ax = plt.subplots()
ax.set_xlim((0, 40))
ax.set_ylim((0, 40))
plt.contour(X,Y,a,100)


circle1=plt.Circle((20,20),2, color='r')
ax.add_artist(circle1)
plt.show()
#print 2Dmat
    
#f=open("data.txt","x")
#i,j=isOneReach(80,80,20*math.pi/180,78, 83, 0.471238898038)
#print i,j
#a=dist([1,1], [0,0])
#print a
#r=input("r=")
#w=input("w=")
#d1=input("d1=")
#d2=input("d2=")

#x1=50
#x2=50
#x3=10*math.pi/180

#dx1=-w*r+d1*math.cos(x3)+w*x2
#dx2=d1*math.sin(x3)-w*x1
#dx3=d2-w

#x=x1+dx1
#y=x2+dx2
#t=x3+dx3

#print x
#print y
#print t
