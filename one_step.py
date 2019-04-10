#!/usr/bin/env python 
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

w_l=[0.1,0.2,0.5,0.7]
w_a=[-1.08,-1.622,-2.432,-3.24,1.08,1.622,2.432,3.24]
R=[5,10,15]
W_a=np.zeros((3,8),dtype=np.float)
W_a[0]=[x/(5*2*math.pi) for x in w_a]
W_a[1]=[x/(10*2*math.pi) for x in w_a]
W_a[2]=[x/(15*2*math.pi) for x in w_a]

#X=[80]
#Y=[80]
theta=range(0,40)
theta=[T*math.pi/20 for T in theta]


d1_max=0.7
d2_max=3.24/(10*math.pi)
#w_max=0.7

#fig=plt.figure()
#ax=plt.axes()

#V=np.ones((100,100),dtype=np.float)

def isOneReach(x,y,t,xx,yy,tt):
    dx=xx-x
    dy=yy-y
    dt=tt-t
    
    if t==0:
        t=0.001
    if t==math.pi/2:
        t=math.pi/2-0.001
    i=0
    i_valid=-1
    for r in range(0,3):
        w=0
        for w_ni in W_a[i]:
            #w_ni[i]=(dx*math.tan(t)-dy)/(x+y*math.tan(t)-r*math.tan(t))
            #if math.fabs(w_ni[i])<=wa_max[i] and w_ni[i]!=0:
            d2_i=w_ni+dt
            d1_i=(dx+R[r]*w_ni-w_ni*y)/math.cos(t)
            d1_i2=(dy+w_ni*x)/math.sin(t)
            e=d1_i-d1_i2
            if d1_i>0 and d1_i2>0 and d1_i<=d1_max and math.fabs(d2_i)<=d2_max and math.fabs(e)<1:
                i_valid=i
                #print xx,yy,tt
                #print "dx",dx,"dy",dy
                #V[yy][xx]=V[yy][xx]+1
                #print "REACHED!!!!!"
                #print i, " w_ni ", w_ni, " d1 ", d1_i, " d2 ", d2_i
                return r+1,w
            w=w+1 
            if w==4:
                w=0
        i=i+1
    if i_valid==-1:
        w=0
        for w_n in w_l:
        #w_n=dy*math.cos(t)/math.sin(t)-dx
            d1_line=(dx+w_n)/math.cos(t)
            d1_line2=dy/math.sin(t)
            e=d1_line-d1_line2
            d2_line=dt
#                            if math.fabs(w_n)<=w_max and w_n!=0 and d1_line>0 and d1_line<=d1_max and math.fabs(d2_line)<=d2_max:
            if d1_line>0 and d1_line2>0 and d1_line<=d1_max and math.fabs(d2_line)<=d2_max and math.fabs(e)<1:
                #print "line w_n ", w_n, " d1_line ", d1_line, " d2_line ", d2_line
                #print xx,yy,tt
                #V[yy][xx]=V[yy][xx]+1
                #print "REACHED!!!!!"
                return 0,w
            w=w+1
    return -1,-1
	        	    
		    

	    
	
