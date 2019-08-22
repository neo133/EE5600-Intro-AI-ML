import matplotlib.pyplot as plt
import numpy as np
import math 
  
# Function to calculate distance 
def distance(x1 , y1 , x2 , y2): 
  
    # Calculating distance 
    return math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0) 
  
# Drivers Code 


def line_gen(A,B):
  len =2
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-2,2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

a=[]
b=[]
# y=0
# x=-50
P = np.array([9, 3*np.sqrt(3)])
y = np.linspace(-10,10,100)
xl = np.linspace(-2,11,100)
Q= np.array([10.5,0])
S = np.array([0.75,0])
# print(S[0])
x = (y**2)/3
yl= (1/np.sqrt(3))*xl
x_PQ = line_gen(P,Q)
x_SQ = line_gen(S,Q)
d = np.linalg.norm(S-Q)
print("Distance SQ = {}".format(d))
# print(d)

plt.figure()

plt.plot(x,y)
plt.plot(xl,yl,label='$OP$')
plt.plot(9,3*np.sqrt(3),'o')
plt.plot(P[0],P[1])
plt.text(P[0]+.9,P[1]-0.5,'$P$(9,5.196)')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_SQ[0,:],x_SQ[1,:],label='$SQ$')
plt.plot(0.75,0,'o')
plt.text(S[0]+0.6,S[1]-0.9,'$S$(0.75,0)')
plt.plot(10.5,0,'o')
plt.text(Q[0]+0.6,Q[1]-0.9,'$Q$(10.5,0)')
plt.plot(0,0,'o')
plt.text(0-1.9,0+0.5,'$O$(0,0)')
plt.text(0+2,0-8,'Distance $SQ$ = 9.75')
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
# plt.gca().set_aspect('equal')
plt.grid()
plt.show()