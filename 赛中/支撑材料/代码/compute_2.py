# 作废比
import numpy as np
import pandas as pd

data = pd.read_excel('C:\\Users\\10049\\Desktop\\1.xlsx', '进项发票信息', usecols=(0, 2, 6, 7))
sale = pd.read_excel('C:\\Users\\10049\\Desktop\\1.xlsx', '销项发票信息', usecols=(0, 2, 6, 7))

data.set_index('企业代号', inplace=True)
sale.set_index('企业代号', inplace=True)


def search_t(data_f, l1, l2):
    for i in data_f.index.unique():
        l1.append(i)
        data_1 = data_f.loc[i]
        b = 0
        for j in data_1['发票状态']:
            if '作废发票' == j:
                b += 1
        l2.append(b / len(data_1))


l_1 = []
l_2 = []
search_t(data, l_1, l_2)
print(l_1)
print(l_2)

data_out = pd.DataFrame({
    '企业': l_1,
    '进项发票作废比': l_2,
})

print(data_out)

l_3 = []
search_t(sale, l_1, l_3)
ser = pd.Series(l_3)
data_out['销项发票作废比'] = ser

print(data_out)
data_out.to_excel('C:\\Users\\10049\\Desktop\\建模文件\\f1作废比.xlsx')
