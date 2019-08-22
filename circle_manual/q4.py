import numpy as np
import math
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if
#setting up plot

#Circle parameters
V = np.eye(2)
u = np.array([1,0])
F = -1
#defining centre and radius of Circle C1
c=u
r=1

#Generating points on the circle C1
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + c).T

#defining centre and radius of Circle C2
c_2=np.array([3,4])
r_2=1


#Generating points on the circle C2
x2_circ = np.zeros((2,len))
x2_circ[0,:] = r_2*np.cos(theta)
x2_circ[1,:] = r_2*np.sin(theta)
x2_circ = (x2_circ.T + c_2).T

#plotting circle C1
plt.figure()
plt.plot(x_circ[0,:],x_circ[1,:],label='$C_1$')

#plotting circle C2
plt.plot(x2_circ[0,:],x2_circ[1,:],label='$C_2$')


#Plotting all points
#plt.plot(p[0], p[1], 'o')
#plt.text(p[0] * (1 + 0.1), p[1] * (1 - 0.1) , 'p')
#c = np.acray(c.T)[0]
plt.plot(c[0], c[1], 'o')
plt.text(c[0] * (1 + 0.1), c[1] * (1-0.1) , 'O1')
plt.plot(c_2[0], c_2[1], 'o')
plt.text(c_2[0] * (1 + 0.1), c_2[1] * (1-0.1) , 'O2')
# ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.gca().set_aspect('equal')

#if using termux
#plt.savefig('../figs/circle.pdf')
#plt.savefig('../figs/circle.eps')
#subprocess.run(shlex.split("termux-open ../figs/circle.pdf"))
#else
plt.show()