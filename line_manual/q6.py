import numpy as np
import matplotlib.pyplot as plt

def line_intersect(p,q):
	P = np.matrix([[p[0][0],-1],[q[0][0],-1]])
	c = -np.matrix([[p[1][0]],[q[1][0]]])
	return np.linalg.inv(P)*c	

def line_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-1,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

A = np.array([0,0])
B = np.array([2,0])
C = np.array([2,2])
D = np.array([0,2])

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

# plt.figure()
# plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
# plt.plot(x_BC[0,:],x_BC[1,:],label='$GH$')
# plt.plot(x_CD[0,:],x_CD[1,:],label='$AB$')
# plt.plot(x_DA[0,:],x_DA[1,:],label='$GH$')
# plt.xlabel('$x$')
# plt.ylabel('$y$')
# plt.legend(loc='best')
# plt.grid()
# plt.show()

# rot = np.array([[0.866,-0.5],[0.5,0.866]])
rot = np.array([[0.866,0.5],[-0.5,0.866]])
newA= np.matmul(A,rot)
newB= np.matmul(B,rot)
newC= np.matmul(C,rot)
newD= np.matmul(D,rot)

nx_AB = line_gen(newA,newB)
nx_BC = line_gen(newB,newC)
nx_CD = line_gen(newC,newD)
nx_DA = line_gen(newD,newA)

plt.figure()
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$GH$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$AB$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$GH$')
plt.plot(nx_AB[0,:],nx_AB[1,:],label='$AB$')
plt.plot(nx_BC[0,:],nx_BC[1,:],label='$GH$')
plt.plot(nx_CD[0,:],nx_CD[1,:],label='$AB$')
plt.plot(nx_DA[0,:],nx_DA[1,:],label='$GH$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()