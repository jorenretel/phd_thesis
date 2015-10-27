from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("white")
sns.set_context("paper")
sns.set(style="ticks", font="serif")

tolx = 1
toly = 1

k = 0.4




top = -1.0/(k**2-1)

fig = plt.figure()
ax = fig.gca(projection='3d')
Xs = np.arange(-1*tolx, tolx+0.1, 0.1)
Ys = np.arange(-1*toly, toly+0.1, 0.1)
X, Y = np.meshgrid(Xs, Ys)
print Xs
print Ys

cmap = sns.dark_palette("#1b9e77", as_cmap=True)

Z2 = []
Z = []
for y in Ys :
  row = []
  row2 = []
  for x in Xs :

    z =max(-1,((((y/toly)**2-1)*top) + (((x/tolx)**2-1)*top))/2.0) #*-1
    row.append(z)
    row2.append(0.0)


  Z.append(row)
  Z2.append(row2)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap,
        linewidth=0, antialiased=False,vmin=-1)

cset = ax.contourf(X, Y, Z, zdir='z', offset=-1.5, cmap=cmap)
ax.set_zlim(-1.5,0)

ax.set_xlabel('fraction of c.s. tolerance x')
ax.set_ylabel('fraction of c.s. tolerance y')
ax.set_zlabel('energy')

#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.savefig('flat_bottom_scoring_function.svg')
#plt.show()