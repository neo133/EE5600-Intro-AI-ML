import numpy as np
import math
import matplotlib.pyplot as plt
from coeffs import *

def line_gen(A,B):
  len =2
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-2,2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

aq= np.array(([2,1],[1,-1]))
a = np.linalg.inv(aq)
# print(a)
h = np.array([3,1])
# u = -np.matmul(a,h)
# print(u)
u=np.array([-2,2])

#Circle parameters
V = np.eye(2)
# u = -np.array([1,0])
F = -1

#defining centre and radius of Circle C1
c=u
print(c)
r=2
print(r)
# r=1.68
#Generating points on the circle C1
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + c).T

A= np.array([-5,0])
B = np.array([0,3.34])

T = line_gen(A,B)

# #Tangent
# p = np.array([1,-1])
# n = u + np.matmul(V.T,p)
# m = np.matmul(omat,n)
# b = F + np.matmul(p.T,u)
# #Generating points on the tangent T
# T = line_dir_pt(m,p,-3,4)

# X /= np.linspace(-1,2,10)
# Y = np.linspace(-1,2,10)
o = np.array([1,-1])


#plotting circle C1
plt.plot(x_circ[0,:],x_circ[1,:],label='$C_1$')
#plotting tangent T
plt.plot(T[0,:],T[1,:],label='Diameter line')
plt.plot(-2,2,'o')
# plt.plot(1.33333333, 0.33333333,'o')
# plt.plot(o[0],o[1],'o',label='point')

# ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
