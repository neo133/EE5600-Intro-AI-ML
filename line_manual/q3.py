import numpy as np
import matplotlib.pyplot as plt
# from coeffs import *

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-3,3,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

A = np.array([-1,0]) 
B = np.array([0,1])

G = np.array([0.71, 0])
H = np.array([0,-5]) 

I = np.array([3,0]) 
J = np.array([0,-3])

K = np.array([-2.14, 0])
L = np.array([0,15])

# A = np.array([2.5,0]) 
# B = np.array([0,3.34])

# G = np.array([-0.625, 0])
# H = np.array([0,-0.84]) 

x_AB = line_gen(A,B)
x_GH = line_gen(G,H)
x_IJ = line_gen(I,J)
x_KL = line_gen(K,L)

#This program calculates the
#intersection of AD and CF
import numpy as np
import matplotlib.pyplot as plt

# def mid_pt(B,C):
# 		D = (B+C)/2
# 		return D


def line_intersect(p,q):
	P = np.matrix([[p[0][0],-1],[q[0][0],-1]])
	c = -np.matrix([[p[1][0]],[q[1][0]]])
	return np.linalg.inv(P)*c	



def line_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

# A = np.matrix('-2;-2')
# B = np.matrix('1;3')
# C = np.matrix('4;-1')

A = np.matrix('-1;0') 
B = np.matrix('0;1')

G = np.matrix('0.71; 0')
H = np.matrix('0;-5') 

I = np.matrix('3;0') 
J = np.matrix('0;-3')

K = np.matrix('-2.1428; 0')
L = np.matrix('0;15')


# D = mid_pt(B,C)
# F = mid_pt(A,B)

a = line_coeff(A,B)
b = line_coeff(G,H)

c = line_coeff(I,J)
d = line_coeff(K,L)

e = line_coeff(A,B)
f = line_coeff(K,L)

g = line_coeff(G,H)
h = line_coeff(I,J)


print("vertices of rohmbus:")
print(line_intersect(a,b))
print(line_intersect(c,d))
print(line_intersect(e,f))
print(line_intersect(g,h))


plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_GH[0,:],x_GH[1,:],label='$GH$')
plt.plot(x_IJ[0,:],x_IJ[1,:],label='$AB$')
plt.plot(x_KL[0,:],x_KL[1,:],label='$GH$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()




