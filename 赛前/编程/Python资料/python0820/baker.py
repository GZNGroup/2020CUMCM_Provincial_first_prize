import numpy as np

x = np.linspace(0, 2*np.pi, 50)  # x坐标函数
# y = 1 / (x + 1)**2
y = np.cos(2*x) * np.exp(-x/5)  # y坐标函数
z = np.column_stack((x, y))  # 数据组成矩阵

# np.savetxt('testdata.txt', z, delimiter='\t')  # 输出txt文件
np.savetxt('testdata.txt', z, delimiter='\t', fmt='%1.4f',
           header='Testing data', footer='End of data')  # 输出txt文件
