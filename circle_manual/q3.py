import numpy as np
import math
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
# import subprocess
# import shlex
# #end if


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

#Circle parameters
V = np.eye(2)
u = -np.array([0,0])
F = -1

# import numpy as np
# import matplotlib.pyplot as plt
# from coeff import *

A = np.array([4,7]) 
B = np.array([2,-5]) 

x_AB = line_gen(A,B)
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')



#defining centre and radius of Circle C1
c=-u
r=3

#Generating points on the circle C1
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + c).T

#plotting circle C1
plt.plot(x_circ[0,:],x_circ[1,:],label='$C_1$')
plt.plot(4,7,'o')


#Plotting all points
#plt.plot(p[0], p[1], 'o')
#plt.text(p[0] * (1 + 0.1), p[1] * (1 - 0.1) , 'p')
#c = np.acray(c.T)[0]
plt.plot(c[0], c[1], 'o')
plt.text(c[0] * (1 + 0.1), c[1] * (1-0.1) , 'c')

ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
#plt.savefig('../figs/circle.pdf')
#plt.savefig('../figs/circle.eps')
#subprocess.run(shlex.split("termux-open ../figs/circle.pdf"))
#else
plt.gca().set_aspect('equal')

plt.show()

