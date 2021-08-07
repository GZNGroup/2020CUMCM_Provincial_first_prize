# 多项式拟合
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel('C:\\Users\\10049\\Desktop\\f3.xlsx', sheet_name='Sheet1')
# print(data)
# print('协方差:\n', data.cov(), '\n')
# print('相关系数:\n', data.corr(), '\n')
x = data.loc[1:, '贷款年利率'].to_list()
y = data.loc[1:, '客户流失率'].to_list()

# y1 = data.loc[1:, 'Unnamed: 2'].to_list()
# y2 = data.loc[1:, 'Unnamed: 3'].to_list()

a = np.polyfit(x, y, 3)
# a1 = np.polyfit(x, y1, 3)
# a2 = np.polyfit(x, y2, 3)
b = np.poly1d(a)
# b1 = np.poly1d(a1)
# b2 = np.poly1d(a2)
c = b(x)
# c1 = b1(x)
# c2 = b2(x)
plt.scatter(x, y, marker='o', label='Credit rating A')
plt.plot(x, c, ls='--', c='blue', label='fitting with three-degree polynomial')
plt.legend()

# plt.scatter(x, y1, marker='o', label='Credit rating B')
# plt.plot(x, c1, ls='--', c='red', label='fitting with three-degree polynomial')
# plt.legend()
#
# plt.scatter(x, y, marker='o', label='Credit rating C')
# plt.plot(x, c2, ls='--', c='green', label='fitting with three-degree polynomial')
# plt.legend()
#
# plt.show()

print('red: ', b, '\n')
# print('blue: ', b1, '\n')
# print('green: ', b2, '\n')
