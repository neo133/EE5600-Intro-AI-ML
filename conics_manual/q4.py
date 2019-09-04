import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

x = np.linspace(-4, 7, 400)
y = np.linspace(-10, 3, 400)

x2 = np.linspace(-14, 17, 400)
y2 = np.linspace(-19, 13, 400)

x, y = np.meshgrid(x, y)
x3, y3 = np.meshgrid(x2, y2)

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
# T2 = line_gen(a2,b2)
# T3 = line_gen(a1,b2)
# T4 = line_gen(a2,b1)
x1 = np.linspace(-15, 15, 1000)
y1 = np.linspace(-15, 15, 1000)
x5, y5 = np.meshgrid(x1, y1)

a = 1.
b = np.sqrt(3)
axes()
# plt.contour(x, y,(x**2/a**2 - y**2/b**2), [1], colors='k')
proxy = plt.contour(x, y,(x**2 + y**2 - 4*x +8*y +12 ), [1], colors='k')
proxy1 = plt.contour(x3, y3,(x3**2 + (y3+6)**2 -1), [1], colors='b')
proxy2 = plt.contour(x5, y5,(y5**2-(8*x5)), [1], colors='b')
# plt.legend(proxy1, ["given","solution","given parabola"])
# plt.legend(proxy2, ["solution"])
# plt.legend(proxy3, ["given parabola"])
plt.plot(2,-4,'o')
plt.plot(0,-6,'o')
# plt.plot(y1, x1)
plt.legend()
plt.gca().set_aspect('equal')
plt.grid()
plt.show()

