import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import pandas as pd


df = pd.read_csv("/content/b_2_2 XYZ")
a = df.iloc[:, 0]
b = df.iloc[:, 1]
c = df.iloc[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=0, azim=50, roll=0)
ax.plot_trisurf(a, b, c, color='white', edgecolors='black', alpha=0.5)
ax.scatter(a, b, c, c='red')
plt.title('b_2_2')
ax.set_xlabel('x');
ax.set_ylabel('y');
ax.set_zlabel('z');



df = pd.read_csv("/content/b_3 XYZ")
a = df.iloc[:, 0]
b = df.iloc[:, 1]
c = df.iloc[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=0, azim=50, roll=0)
ax.plot_trisurf(a, b, c, color='white', edgecolors='black', alpha=0.5)
ax.scatter(a, b, c, c='red')
plt.title('b_3')
ax.set_xlabel('x');
ax.set_ylabel('y');
ax.set_zlabel('z');



df = pd.read_csv("/content/e_2_2 XYZ")
a = df.iloc[:, 0]
b = df.iloc[:, 1]
c = df.iloc[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=0, azim=50, roll=0)
ax.plot_trisurf(a, b, c, color='white', edgecolors='black', alpha=0.5)
ax.scatter(a, b, c, c='red')
plt.title('e_2_2')

ax.set_xlabel('x');
ax.set_ylabel('y');
ax.set_zlabel('z');



df = pd.read_csv("/content/e_3 XYZ")
a = df.iloc[:, 0]
b = df.iloc[:, 1]
c = df.iloc[:, 2]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=0, azim=50, roll=0)
ax.plot_trisurf(a, b, c, color='white', edgecolors='black', alpha=0.5)
ax.scatter(a, b, c, c='red')
plt.title('e_3')

ax.set_xlabel('x');
ax.set_ylabel('y');
ax.set_zlabel('z');

