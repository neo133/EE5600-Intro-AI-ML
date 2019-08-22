
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

A = np.array([4,0])
B = np.array([0,-4])

f = np.array([-1,0])
g= np.array([0,-1])

m = np.array([1,1])
P = np.array([2,1])
omat = np.array([[0,1],[1,0]])
n = np.array([1,-1]) 
d =  2*np.sqrt(3)
# print(d)

# m = np.matmul(omat,n) 

lam = d/(np.linalg.norm(m))
# print(lam)

Q = P - (lam*m)
print(Q)


#Generating all lines
x_AB = line_gen(A,B)
x_PQ = line_gen(P,Q)
x_jk = line_gen(f,g)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$L$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$parallel to L$')
plt.plot(x_jk[0,:],x_jk[1,:],label='$PQ$')
plt.plot(P[0],P[1],'o',label='$point(2,1)$')


'''plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')'''

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()
