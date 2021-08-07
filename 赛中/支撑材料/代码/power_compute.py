# 利润、利润率、订单数
import pandas as pd

data = pd.read_excel('C:\\Users\\10049\\Desktop\\1.xlsx', '进项发票信息', usecols=(0, 2, 6, 7))
sale = pd.read_excel('C:\\Users\\10049\\Desktop\\1.xlsx', '销项发票信息', usecols=(0, 2, 6, 7))
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

sale.set_index('发票状态', inplace=True)
sale_2 = sale.drop(labels='作废发票', axis=0)
sale_2.set_index('企业代号', inplace=True)
sale_1 = sale_2.drop(labels=delete, axis=0)

average_list = []
average_sale = []
average_saleRa = []
average_cov = []
name = []

for i in D.index.to_list():

    a = data_1.loc[i]
    b = sale_1.loc[i]

    if type(a) == pd.Series:
        a = a.to_frame()
        a = pd.DataFrame(a.values.T, columns=a.index)

    if type(b) == pd.Series:
        b = b.to_frame()
        b = pd.DataFrame(b.values.T, columns=b.index)

    a_g = a.groupby('开票日期').sum()
    b_g = b.groupby('开票日期').sum()

    l_a = a_g.index.to_list()
    l_b = b_g.index.to_list()
    time_1 = min(l_a[0], l_b[0])
    time_2 = max(l_a[-1], l_b[-1])
    time_3 = (time_2 - time_1).days / 30

    name.append(i)
    average_list.append(len(b) / time_3)

    sale_money = b_g.sum() - a_g.sum()


    average_sale.append(sale_money.iloc[0])

    average_saleRa.append(sale_money.iloc[0] / a_g.sum().iloc[0])


data_out = pd.DataFrame({
    '企业代号': name,
    '月均订单数': average_list,
    '月均利润': average_sale,
    '月均利润率': average_saleRa,
})

# print(data_out)
# print(data_out['月均订单数'].corr(b['月均利润']))
data_out.to_excel('C:\\Users\\10049\\Desktop\\5.xlsx')
