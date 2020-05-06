import numpy as np
import matplotlib.pyplot as plt

w = np.array([1, -1])  # W(0)
ng = 1  # 学习率1
X = np.array([[1, -2], [0, -1], [2, 3], [1, 1]])


def sig(a):  # 双极性sigmoid函数
    return (1 - np.exp(-a)) / (1 + np.exp(-a))


temp = np.sign(1)

x = np.arange(-10, 10, 0.02)
plt.plot(x, sig(x), 'r')
plt.show()

#  print(temp)


for i in range(4):
    net = np.inner(w, X[i])
    print('net: ', net)
    w = w + ng * sig(net) * X[i]
    print(w)
