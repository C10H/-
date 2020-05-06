import numpy as np


def sig(a):  # 双极性sigmoid函数
    return (1 - np.exp(-a)) / (1 + np.exp(-a))


x = np.array([[2.0, 0, -1], [1.0, -2, -1]])  # 输入
d = [-1, 1]  # 教师信号
ng = 0.25  # learning rate
w = np.array([1.0, 0, 1])  # w(0)

for i in range(2):
    net = np.inner(w, x[i])
    print('net: ', net)
    w += ng * (d[i] - net) * x[i]
    print('w: ', w)
