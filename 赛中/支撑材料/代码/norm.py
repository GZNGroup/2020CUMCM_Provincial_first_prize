# 归一化
import numpy as np
import pandas as pd

data = pd.read_excel('C:\\Users\\10049\\Desktop\\建模文件\\power3.xlsx', 'Sheet1')

# 数据归一化处理
min = data['power'].min()
max = data['power'].max()

l1 = []
for i in data['power']:
    l1.append((i - min) / (max - min))

ser = pd.Series(l1)

data.loc[:, 'power归一化'] = ser

data.set_index('企业代号', inplace=True)

print(data)
data.to_excel('C:\\Users\\10049\\Desktop\\建模文件\\power_f3.xlsx', 'Sheet1')
