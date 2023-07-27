import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import pandas as pd

df = pd.read_csv("/content/b_2_2 XYZ")
a = df.iloc[:, 0]
b = df.iloc[:, 1]
c = df.iloc[:, 2]

df = pd.read_csv("/content/b_3 XYZ")
d = df.iloc[:, 0]
e = df.iloc[:, 1]
f = df.iloc[:, 2]


df = pd.read_csv("/content/e_2_2 XYZ")
g = df.iloc[:, 0]
h = df.iloc[:, 1]
i = df.iloc[:, 2]

df = pd.read_csv("/content/e_3 XYZ")
j = df.iloc[:, 0]
k = df.iloc[:, 1]
l = df.iloc[:, 2]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=8, azim=30, roll=20)

ax.plot_trisurf(a, b, c, color='white', edgecolors='black', alpha=0.5)

ax.plot_trisurf(d, e, f, color='black', edgecolors='black', alpha=0.5)

ax.plot_trisurf(g, h, i, color='blue', edgecolors='black', alpha=0.5)

ax.plot_trisurf(j, k, l, color='yellow', edgecolors='black', alpha=0.5)

ax.scatter(a, b, c, c='red')
ax.scatter(d, e, f, c='blue')
ax.scatter(g, h, i, c='green')
ax.scatter(j, k, l, c='yellow')




