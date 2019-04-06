#!/usr/bin/env python
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

def dist(a,b):
    d=math.sqrt((a[0]-b[0])^2+(a[1]-b[1])^2)
    return d;

N=6
r=5
V=np.ones((100,100,40),dtype=np.float)
print V
print np.size(V)
for n in range(1,7):
    for q in range(1,2):
        for theta in range(1,41):
            for x in range(1,101):
                for y in range(1,101):
                    if 

fig=plt.figure()
ax=plt.axes(projection='3d')
#ax.scatter3D(range(1,101),range(1,101),
plt.show()
                      
#x=[1,2,3]
#y=[2,4,1]

#plt.plot(x,y)

#plt.xlabel('x-axis')
#plt.ylabel('y-axis')

#plt.show()
print "hello"

