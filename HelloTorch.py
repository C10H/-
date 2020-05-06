"""
本程序为一个练习程序，用神经网络写回归问题
本程序有1个隐层，可以用于拟合二次函数曲线
"""
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

#  构造伪数据
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2 * torch.rand(x.size())


# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()

class Net(torch.nn.Module):

    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()  # 调用父类
        self.hidden = torch.nn.Linear(in_features=n_feature, out_features=n_hidden)  # 定义隐藏层
        self.output = torch.nn.Linear(in_features=n_hidden, out_features=n_output)  # 定义输出层

    def forward(self, x):  # 对应神经网络前向传递数据
        x = F.relu(self.hidden(x))
        x = self.output(x)
        return x


net = Net(1, 10, 1)  # 输入的x为1维，隐藏层有10个神经元，输出y为1维
print(net)  # 打印层结构

plt.ion()   # 实时打印
plt.show()

optimizer = torch.optim.SGD(net.parameters(), lr=0.5)  # Lr是学习率
loss_func = torch.nn.MSELoss()

for t in range(100):    # 训练过程， 训练100步
    prediction = net(x)  # 计算输出prediction
    loss = loss_func(prediction, y)  # 将输出prediction与教师信号y作对比，计算误差

    optimizer.zero_grad()
    loss.backward()  # 误差反传
    optimizer.step()

    # 展示神经网络的优化过程
    if t % 5 == 0:
        plt.cla()   # 清屏
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        # plt.text(0.5, 0, 'Loss=%.4f' % loss[0], fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)

plt.ioff()
plt.show()