import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Triangle vertices
A = np.array([2.5,0]) 
B = np.array([0,3.33]) 

C = np.array([-0.625,0])
D = np.array([0,-0.84])

#Generating all lines
x_AB = line_gen(A,B)
x_CD = line_gen(C,D)
X = np.linspace(-1,2,10)
Y = np.linspace(-1,2,10)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(X,Y)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()
