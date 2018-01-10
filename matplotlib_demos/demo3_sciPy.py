import scipy as sp
import matplotlib.pylab as plt
#Next, we can define some points on the (0, 1) interval with:
t = sp.linspace(0, 1, 100)
#Now, let’s plot a parabola defined by the above interval:
plt.plot(t, t**2)
plt.show()
