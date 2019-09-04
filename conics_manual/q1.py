import matplotlib.pyplot as plt
import numpy as np

def line_gen(A,B):
  len =2
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-9,9,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

A = np.array([-0.09,0])
B = np.array([0,-0.09])
T = line_gen(A,B)

# create 1000 equally spaced points between -10 and 10
x = np.linspace(-1, 1, 1000)
# y = np.linspace(-10, 10, 1000)

# calculate the y value for each element of the x vector
y1 = 3*(x**2) 

fig, ax = plt.subplots()
ax.plot(T[0,:],T[1,:],label='$T$')
ax.plot(x, y1)
ax.plot(y1, x)
plt.grid()
plt.show()