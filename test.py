#!/usr/bin/env python 
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#V=np.ones((5,5,5),dtype=np.float)

#print V[:][:][4]

w_l=[0.1,0.2,0.5,0.7]
w_a=[1.08,1.622,2.432,3.24]
R=[5,10,15]

w_a1=[x/(5*2*math.pi) for x in w_a]
w_a2=[x/(10*2*math.pi) for x in w_a]
#w_a2=w_a/(10*2*math.pi)
w_a3=[x/(15*2*math.pi) for x in w_a]
wa_max=[w_a1[3],w_a2[3],w_a3[3]]
#w_a3=w_a/(15*2*math.pi)
print "wa_max ", wa_max
X=[80]
Y=[80]
theta=range(0,40)
theta=[T*math.pi/40 for T in theta]
t=20*math.pi/180
print "t=",t
d1_max=0.7
d2_max=3.24/(10*math.pi)
w_max=0.7
w_ni=np.zeros((3),dtype=np.float)
d1_i=np.zeros((3),dtype=np.float)
d2_i=np.zeros((3),dtype=np.float)

fig=plt.figure()
ax=plt.axes()

V=np.ones((100,100),dtype=np.float)
#for t in theta:
for x in X:
    for y in Y:
        for tt in theta:
            for xx in range(0,100):
                for yy in range(0,100):
                    #print xx,yy,tt
                    dx=xx-x
                    dy=yy-y
                    dt=tt-t
                    i=0
                    i_valid=-1
                    for r in R:
                        #print "Checking radius ", r
                        w_ni[i]=(dx*math.tan(t)-dy)/(x+y*math.tan(t)-r*math.tan(t))
                        #print
                        if math.fabs(w_ni[i])<=wa_max[i] and w_ni[i]!=0:
                            d2_i[i]=w_ni[i]+dt
                            d1_i[i]=(dx+r*w_ni[i]-w_ni[i]*y)/math.cos(t)
                            if d1_i[i]>0 and d1_i[i]<=d1_max and math.fabs(d2_i[i])<=d2_max:
                                i_valid=i
                                print xx,yy,tt
                                V[xx][yy]=V[xx][yy]+1
                                print "REACHED!!!!!"
                                print i, " w_ni ", w_ni[i], " d1 ", d1_i[i], " d2 ", d2_i[i]
                        i=i+1
                    if i_valid==-1:
                        #print "not arc mode. checking line mode"
                        w_n=dy*math.cos(t)/math.sin(t)-dx
                        d1_line=(dx+w_n)/math.cos(t)
                        d2_line=dt
                        if math.fabs(w_n)<=w_max and w_n!=0 and d1_line>0 and d1_line<=d1_max and math.fabs(d2_line)<=d2_max:
                            print "line w_n ", w_n, " d1_line ", d1_line, " d2_line ", d2_line
                            print xx,yy,tt
                            V[xx][yy]=V[xx][yy]+1
                            print "REACHED!!!!!"
                        #else:
                            #print "not reachable!!!!"
print "done"
ax.contour(range(0,100),range(0,100),V,10)    
plt.show()
	        	    
		    

	    
	
