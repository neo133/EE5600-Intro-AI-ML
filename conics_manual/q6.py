import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

x = np.linspace(-9, 9, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)

def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)

def line_gen(A,B):
  len =2
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(-5,5,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

A = np.array([9/5,0])
B = np.array([0,0])
T1 = line_gen(A,B)

a = 3
b = 4
axes()
plt.contour(x, y,(x**2/a**2 - y**2/b**2), [1], colors='b')
plt.plot(T1[1,:],T1[0,:],label='$directrix$')
plt.legend()
plt.grid()
plt.show()
