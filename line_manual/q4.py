import numpy as np
import matplotlib.pyplot as plt

# def line_intersect(p,q):
# 	P = np.matrix([[p[0][0],-1],[q[0][0],-1]])
# 	c = -np.matrix([[p[1][0]],[q[1][0]]])
# 	return np.linalg.inv(P)*c	

def line_coeff(A,B):
	p = np.zeros((2,1))
	p[0] = (A[1]-B[1])/(A[0]-B[0])
	p[1] = (A[0]*B[1]-A[1]*B[0])/(A[0]-B[0])
	return p

def line_gen(A,B):
  len =20
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-1,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

k =2
g= np.array([k,-3*k])
h= np.array([5,k])
i = np.array([-k,2])
m = np.matrix(([k, 5, -k],[-3*k,k,2],[1,1,1]))

A= np.array(([5+k,k-2],[2*k,-2-(3*k)]))
a = np.linalg.inv(A)
# print(a)
c= k*np.array([11-(4*k),8-(3*k)])
b = np.matmul(a,c)
print("orthocentre: ")
print(b)
print("area: ")
f = np.linalg.det(m)
print(f)

x_gh = line_gen(g,h)
x_hi = line_gen(h,i)
x_ig = line_gen(i,g)

plt.figure()
plt.plot(x_gh[0,:],x_gh[1,:],label='$AB$')
plt.plot(x_hi[0,:],x_hi[1,:],label='$GH$')
plt.plot(x_ig[0,:],x_ig[1,:],label='$AB$')
plt.plot(b[0],b[1],'o',label='orthocentre')
# plt.plot(x_DA[0,:],x_DA[1,:],label='$GH$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
