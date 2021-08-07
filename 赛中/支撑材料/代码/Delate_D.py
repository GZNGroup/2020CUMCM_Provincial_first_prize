import pandas as pd
import numpy as np

data = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\副本.xlsx', '进项发票信息')
sale = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\副本.xlsx', '销项发票信息')

D = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\1.xlsx', '企业信息')
# 剔除D评级企业
delete = []
for i in range(123):
    if D.iloc[i, 2] == 'D':
        delete.append(D.iloc[i, 0])

D.set_index('企业代号', inplace=True)
D = D.drop(labels=delete, axis=0)

data.set_index('发票状态', inplace=True)
data_2 = data.drop(labels='作废发票', axis=0)
data_2.set_index('企业代号', inplace=True)
data_1 = data_2.drop(labels=delete, axis=0)

sale.set_index('发票状态', inplace=True)
sale_2 = sale.drop(labels='作废发票', axis=0)
sale_2.set_index('企业代号', inplace=True)
sale_1 = sale_2.drop(labels=delete, axis=0)

with pd.ExcelWriter('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\去掉D之后.xlsx') as writer:
    D.to_excel(writer, sheet_name='企业信息')
    data_1.to_excel(writer, sheet_name='进项')
    sale_1.to_excel(writer, sheet_name='销项')
