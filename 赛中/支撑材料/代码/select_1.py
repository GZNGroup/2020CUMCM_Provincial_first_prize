# 供求稳定、筛选、利润
import numpy as np
import pandas as pd

data = pd.read_excel('C:\\Users\\10049\\Desktop\\f2.xlsx', '进项发票信息', usecols=(0, 2, 6, 7))
sale = pd.read_excel('C:\\Users\\10049\\Desktop\\f2.xlsx', '销项发票信息', usecols=(0, 2, 6, 7))
D = pd.read_excel('C:\\Users\\10049\\Desktop\\1.xlsx', '企业信息', usecols=(0, 2))
# 剔除D评级企业
delete = []
for i in range(123):
    if D.iloc[i, 1] == 'D':
        delete.append(D.iloc[i, 0])

D.set_index('企业代号', inplace=True)
D = D.drop(labels=delete, axis=0)

data.set_index('发票状态', inplace=True)
data_2 = data.drop(labels='作废发票', axis=0)
data_2.set_index('企业代号', inplace=True)
data_1 = data_2.drop(labels=delete, axis=0)

# data_1.to_excel('C:\\Users\\10049\\Desktop\\2.xlsx')

sale.set_index('发票状态', inplace=True)
sale_2 = sale.drop(labels='作废发票', axis=0)
sale_2.set_index('企业代号', inplace=True)
sale_1 = sale_2.drop(labels=delete, axis=0)

# sale_1.to_excel('C:\\Users\\10049\\Desktop\\3.xlsx')

l1 = []
l2 = []
l3 = []
ser = pd.Series([' '])
for i in D.index.to_list():
    a = data_1.loc[i]
    b = sale_1.loc[i]

    if type(a) == type(ser):
        a = a.to_frame()
        a = pd.DataFrame(a.values.T, columns=a.index)

    if type(b) == type(ser):
        b = b.to_frame()
        b = pd.DataFrame(b.values.T, columns=b.index)

    a_g = a.groupby('开票日期').sum()
    b_g = b.groupby('开票日期').sum()

    l_a = a_g.index.to_list()
    l_b = b_g.index.to_list()
    time_1 = min(l_a[0], l_b[0])
    time_2 = max(l_a[-1], l_b[-1])
    pda = pd.date_range(start=time_1, end=time_2, freq='M')
    # pd = pd.date_range(start=time_1, end=time_2)
    a_t = a_g.reindex(pda, fill_value=0)
    b_t = b_g.reindex(pda, fill_value=0)
    #
    for j in pda:
        j = str(j)[0:7]
        l1.append(i)
        l2.append(j)
        print(i, ' ', j)
        l3.append((b_t.loc[j].sum() - a_t.loc[j].sum()).iloc[0])
        print((b_t.loc[j].sum() - a_t.loc[j].sum()).iloc[0])

data_out = pd.DataFrame({
    '企业代号': l1,
    '开票时间（月）': l2,
    '销进差': l3
})
print(data_out)
data_out.describe()
# data_out.to_excel('C:\\Users\\10049\\Desktop\\盈利趋势.xlsx')
l1 = []
l2 = []
l3 = []
data_out.set_index('企业代号', inplace=True)
for i in data_out.index.unique():
    a = data_out.loc[i, '销进差']
    b = a.describe()
    l1.append(i)
    l2.append(a.std())

for i in l2:
    l3.append((i-np.min(l2))/(np.max(l2)-np.min(l2)))

data_o = pd.DataFrame({
    '企业代号': l1,
    '标准差': l2,
    '标志差（归一化）': l3
})

print(data_o)
data_o.to_excel('C:\\Users\\10049\\Desktop\\4.xlsx', sheet_name='Sheet2')
