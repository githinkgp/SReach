#!/usr/bin/env python 
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from dist import dist
from one_step import isOneReach


circle1 = plt.Circle((20, 20), 2, color='r')
#circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
#circle3 = plt.Circle((1, 1), 0.2, color='g', clip_on=False)

fig=plt.figure()
ax=plt.axes()
#fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.add_artist(circle1)

ax.set_xlim((0, 40))
ax.set_ylim((0, 40))

#fig.savefig('plotcircles.png')

plt.show()
