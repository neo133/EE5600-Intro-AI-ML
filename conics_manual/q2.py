import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

x = np.linspace(-4, 4, 400)
y = np.linspace(-2, 2, 400)
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

a1 = np.array([1/np.sqrt(2),0])
b1 = np.array([0,-np.sqrt(3)])
a2 = np.array([-5,0])
b2 = np.array([0,-4])

T1 = line_gen(a1,b1)

a = 1.
b = np.sqrt(3)
axes()
plt.contour(x, y,(x**2/a**2 - y**2/b**2), [1], colors='k')
plt.plot(T1[0,:],T1[1,:],label='$Tangent$')
plt.plot(np.sqrt(2),np.sqrt(3),'o')
plt.legend()
plt.show()

