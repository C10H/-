# """
# author: @10181704
# 神经网络4.7节作业
# """
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas
#
# X = np.array([[-1., -1], [1, 1], [1, -1]])  # input
#
# W = np.array([[np.sqrt(2), 0], [0, np.sqrt(2)]])  # W0
#
# ng = 0.5
#
# # 归一化过程
# # 无需归一化
#
# for i in range(3):
#     TrainingPoint = i % 3
#     MaxInner = -2
#     MaxPoint = 0
#     print()
#     print("Training", i + 1)
#     print(X[i])
#     for j in range(2):
#         print('inner', np.inner(X[TrainingPoint], W[j]))
#         if MaxInner < np.inner(X[TrainingPoint], W[j]):  # 寻找胜者
#             MaxInner = np.inner(X[TrainingPoint], W[j])
#             MaxPoint = j
#
#     W[MaxPoint] = W[MaxPoint] - ng * (W[MaxPoint] - X[TrainingPoint])
#     W[MaxPoint] = W[MaxPoint] / np.sqrt(W[MaxPoint][0] ** 2 + W[MaxPoint][1] ** 2) * np.sqrt(2)
#
#     print("result", i + 1)
#     print(TrainingPoint + 1, MaxPoint + 1)
#     print('result W', i + 1)
#     for j in range(2):
#         print(j + 1, ' ', W[j])
#
# for i in range(3):
#     print()
#     for j in range(2):
#         print(np.inner(X[i],W[j]),end=' ')

# s=[i for i in range(1,91)]
# while True:
#
#     n=input()
#     if n=="#":
#         break
#     if n.isdigit()==True:
#         if int(n) in s:
#             s.remove(int(n))
# print(s)


def calc(inpu):
    valu = 0
    for i in inpu:
        if type(i) is int:
            valu += i
        elif type(i) is tuple:
            valu += calc(i)
        elif type(i) is list:
            valu += calc(i)
        else:
            pass
    return valu


lis = eval(input())
print(calc(lis))
