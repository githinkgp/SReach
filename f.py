#!/usr/bin/env python 
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from dist import dist
from one_step import isOneReach


f=open("data.txt","x")
f.write(
#i,j=isOneReach(80,80,20*math.pi/180,78, 83, 0.471238898038)
#print i,j
#a=dist([1,1], [0,0])
#print a
r=input("r=")
w=input("w=")
d1=input("d1=")
d2=input("d2=")

x1=50
x2=50
x3=10*math.pi/180

dx1=-w*r+d1*math.cos(x3)+w*x2
dx2=d1*math.sin(x3)-w*x1
dx3=d2-w

x=x1+dx1
y=x2+dx2
t=x3+dx3

print x
print y
print t
