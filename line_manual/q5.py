import numpy as np
import matplotlib.pyplot as plt

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

x = np.array([[1,1],[1,-1]]) 
y = np.linalg.inv(x) 
b = np.array([2,0])
# print x 
 # print y 
p = np.matmul(y,b)
# print (p)
c = -2*p
# print(c)

cf = np.linalg.norm(c-p)
# print(cf)
ab = cf*2/np.sqrt(3)
arr = 0.5*ab*cf
print(arr)

a= np.array([-2,-2])
b= np.array([-0.732,-0.732])
k= np.array([2.732,-0.732])

x_ab = line_gen(a,b)
x_bk = line_gen(b,k)
x_kd = line_gen(k,a)

plt.figure()
plt.plot(x_ab[0,:],x_ab[1,:],label='$AB$')
plt.plot(x_bk[0,:],x_bk[1,:],label='$AB$')
plt.plot(x_kd[0,:],x_kd[1,:],label='$AB$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()