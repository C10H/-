"""
Author: C10H15N
用于绘制坐标点的小型脚本
20200405 最初用于神经网络作业3/5题
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[5.0, 7, 3, 5], [1, 3, 2, 4]])
y = np.array([[0.0, -1, -2, -3], [0, -3, 3, 0]])

Ex = np.array([np.mean(x[0]), np.mean(x[1])])
Ey = np.array([np.mean(y[0]), np.mean(y[1])])

E = np.array([np.mean([Ex[0], Ey[0]]), np.mean([Ex[1], Ey[1]])])

line_x = np.arange(-1, 3, 0.02)
line_y = -(3 * line_x - 6.5)

test_x = np.array([4, 0, 36/13])
test_y = np.array([2, 5, 0])

print(Ex, Ey)
print(E)

print(x[0], x[1], x[0][0])
print(y[0], y[1])

fig = plt.subplot()

fig.scatter(x=x[0], y=x[1])
fig.scatter(x=y[0], y=y[1])
fig.scatter(Ex[0], Ex[1])
fig.scatter(Ey[0], Ey[1])
fig.plot([Ex[0], Ey[0]], [Ex[1], Ey[1]])
fig.plot(line_x, line_y)
fig.scatter(test_x, test_y)
fig.grid(True, which='both')
fig.axhline(y=0, color='k')
fig.axvline(x=0, color='k')

plt.show()

