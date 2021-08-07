import numpy as np  # 调用NumPy模块
import matplotlib.pyplot as plt  # 调用Matplotlib模块下的pyplot

x = np.linspace(0, 2*np.pi, 50)  # 画图数据横坐标
y = np.sin(x)  # sin函数值
z = np.cos(x)  # cos函数值
u = np.exp(-x)  # e^(-x)函数值

da = np.loadtxt('testdata.txt', delimiter='\t')  # 读取txt文件中的数据
a, b = da[:, 0], da[:, 1]  # 将数据存为a,b两个变量

fig, ax = plt.subplots()  # 创建画图对象fig和ax
# plt.set_cmap('cividis')
plt.set_cmap('rainbow')  # 设定画图颜色主题
# plt.set_cmap('twilight')
ax.plot(x, y, label='sine function')  # 画连续曲线
ax.scatter(x, z, c=z, label='cosine function')  # cosine函数数据点画图
ax.scatter(x, u, c='k', s=50*u+20, alpha=0.5, marker='^', label=r'$e^{-x}$')
ax.scatter(a, b, c='c', s=50*b+50, label=r'$e^{-x/5}cos(2x)$')  # txt文件读取数据画图
ax.set_xlabel('x')  # 设置横坐标的名称
ax.set_ylabel('f(x)')  # 设置纵坐标的名称
ax.set_title(r'sine, cosine $e^{-x}$ and $e^{-\frac{x}{5}}cos(2x)$ function')  # 设置画图标题
ax.set_xticks([0, 0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi])  # 设置横坐标刻度位置
ax.set_xticklabels([0, r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])  # 设置横坐标刻度标签
ax.legend()  # 显示图例说明
ax.grid(c='lightgray', linestyle='--')  # 设置网格线样式
fig.tight_layout()  # 设置紧凑显示图像
plt.minorticks_on()  # 显示坐标小刻度
plt.show()  # 显示图像
