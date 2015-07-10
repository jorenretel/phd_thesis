import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

xs = []
ys = []
zs = []

with open('nuslist', 'r') as f:

    for line in f.readlines():
        x, y, z = line.split()
        xs.append(float(x))
        ys.append(float(y))
        zs.append(float(z))


#sns.set(font='serif')
sns.set_style("white")
rcParams['font.family'] = 'serif'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xs, ys, zs, color=['#377eb8'])   # color=['#2ca25f'])

ax.set_xlabel('1H')
ax.set_ylabel('15N')
ax.set_zlabel('15N')

ax.set_xlim([0, 32])
ax.set_ylim([0, 32])
ax.set_zlim([0, 32])

#sns.set(font='serif')


#plt.savefig('nus_cube.png', dpi=500)
plt.savefig('nus_cube.svg')
