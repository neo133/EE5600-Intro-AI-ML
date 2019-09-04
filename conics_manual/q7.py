import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

x = np.linspace(-11, 11, 400)
y = np.linspace(-9, 11, 400)
x, y = np.meshgrid(x, y)

def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)

def line_gen(A,B):
  len =2
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-2,2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

A1 = np.array([3,0])
B1 = np.array([0,4])
T1 = line_gen(A1,B1)

A2 = np.array([4,0])
B2 = np.array([0,3])
T2 = line_gen(A2,B2)

a = 3
b = 4
axes()
plt.contour(x, y,(7*x*y-6*x-6*y), [1], colors='b')
plt.plot(T1[0,:], T1[1,:],color='r',label='$l1$')
plt.plot(T2[0,:], T2[1,:],label='$l2$')
plt.legend()
plt.grid()
plt.show()
