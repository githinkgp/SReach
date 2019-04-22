#!/usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from array import *
import math
from dist import dist
from one_step import isOneReach

N=6
r=2
V=np.ones((40,40),dtype=np.float)
#print V
w_l=[0.1,0.2,0.5,0.7]
w_a=[-1.08,-1.622,-2.432,-3.24,1.08,1.622,2.432,3.24]
R=[5,10,15]
W_a=np.zeros((3,8),dtype=np.float)
W_a[0]=[x/(5*2*math.pi) for x in w_a]
W_a[1]=[x/(10*2*math.pi) for x in w_a]
W_a[2]=[x/(15*2*math.pi) for x in w_a]
Q=[1]
P=[[0.3,0.2,0.3,0.2],[0.2,0.2,0.3,0.3],[0.2,0.2,0.3,0.3],[0.2,0.2,0.3,0.3]]
theta=range(0,20)
#theta=[T*math.pi/20 for T in theta]
print np.size(V)
for n in range(1,11):
    print "step: ",n
    for q in Q:
        for t in [2]:
            for x in range(0,40):
                for y in range(0,40):
                    #print x,y,t
                    if dist([x,y],[20,20])<=r:
                        V[y][x]=0
                    elif n!=1:
                        for qq in Q:
                            sumX=0
                            for tt in theta:#limit the number of iterations after this by checking the distance to (x,y)
                                for xx in range(x-10,x+10):
                                    if xx>39 or xx<0:
                                        continue
                                    for yy in range(y-10,y+10):
                                        if yy>39 or yy<0 or dist([xx,yy],[20,20])<=r:
                                            continue
                                        i,j=isOneReach(x,y,t*math.pi/10,xx,yy,tt*math.pi/10)
                                        if i==-1 and j==-1:
                                            continue
                                        tau=P[i][j]
                                        v=V[yy][xx]*tau
                                        sumX=sumX+v
                        V[y][x]=sumX
                        
fig=plt.figure()
ax=plt.axes(projection='3d')
count=0
v=np.zeros((40,40),dtype=np.float)
for i in range(0,40):
    for j in range(0,40):
#	ax.scatter3D(i,j,V[i][j][20])
	v[i][j]=V[i][j]
	#print V[i][j][1]
	count=count+1
x=range(0,40)
y=range(0,40)
X,Y=np.meshgrid(x,y)
print count
print V.shape
#print V[:][:][1]
#print np.size(V[:][:][10])
#plt.contour(range(0,100),range(0,100),v,5)
with open('outfile.txt','wb') as f:
    for line in V:
        count=count+1
        np.savetxt(f,line,fmt='%.2f')
ax.plot_surface(X,Y,V)

fig=plt.figure()
ax=plt.axes()
plt.contour(X,Y,V,100)
plt.show()
                      
#x=[1,2,3]
#y=[2,4,1]

#plt.plot(x,y)

#plt.xlabel('x-axis')
#plt.ylabel('y-axis')

#plt.show()
print "hello"

