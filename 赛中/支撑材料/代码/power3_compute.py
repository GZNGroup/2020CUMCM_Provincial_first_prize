# 换算利润
import pandas as pd
import numpy as np

data = pd.read_excel('C:\\Users\\10049\\Desktop\\建模文件\\power_f2.xlsx')
data_1 = pd.read_excel('C:\\Users\\10049\\Desktop\\建模文件\\新冠对行业的影响.xlsx')

data.set_index('企业代号', inplace=True)
data_1.set_index('行业类别')


def fun (b):
    data.loc[i, '月均订单数'] = data.loc[i, '月均订单数'] * b
    data.loc[i, '月均利润'] = data.loc[i, '月均利润'] * b


for i in data.index:
    a = data.loc[i, '行业类别']
    if a in data_1.index:
        fun(data_1.loc[a, '最终系数'])

data.to_excel('C:\\Users\\10049\\Desktop\\建模文件\\power_f3.xlsx')
