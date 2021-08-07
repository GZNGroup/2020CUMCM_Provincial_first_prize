import numpy as np
from baker import tstf
from baker import le2
from baker import le3
from baker import le4
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决中文下负号是方块的问题

kn = np.array([-0.906179845938664, -0.53846931010568, 0,
               0.53846931010568, 0.906179845938664])  # 节点数据
we = np.array([0.236926885056189, 0.478628670499366, 0.568888888888889,
               0.478628670499366, 0.236926885056189])  # 权重数据
y = tstf(kn)  # Gauss节点上函数f（x）的值

# 以下为多项式系数的计算
c0 = 0.5 * sum(we * y)
c1 = 1.5 * sum(we * y * kn)
c2 = 2.5 * sum(we * y * le2(kn))
c3 = 3.5 * sum(we * y * le3(kn))
c4 = 4.5 * sum(we * y * le4(kn))

xx = np.linspace(-1, 1, 41)  # 画图曲线的自变量点
uu = c0 + c1*xx + c2*le2(xx) + c3*le3(xx) + c4*le4(xx)  # 组成拟合曲线的函数值点

fig, ax = plt.subplots()  # 定义画图对象 fig 和 ax
ax.plot(xx, tstf(xx), label=r'$e^{-x}\sin(x)$')  # 画连续图像
ax.scatter(xx, uu, c=uu, marker='^', label="逼近多项式曲线")  # 画散点图像
ax.set_xlabel('x')  # 设置横坐标的名称
ax.set_ylabel('函数值')  # 设置纵坐标的名称
ax.set_title('Legendre多项式逼近')  # 设置画图标题
ax.legend()  # 显示图例说明
ax.grid(c='lightgray', linestyle='--')  # 设置网格线样式
fig.tight_layout()  # 设置紧凑显示图像
plt.minorticks_on()  # 显示坐标小刻度
plt.show()  # 显示图像
