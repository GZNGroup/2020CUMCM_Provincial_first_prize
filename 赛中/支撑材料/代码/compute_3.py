# 负单比
import numpy as np
import pandas as pd

data = pd.read_excel('C:\\Users\\10049\\Desktop\\1.xlsx', '进项发票信息', usecols=(0, 2, 6, 7))
sale = pd.read_excel('C:\\Users\\10049\\Desktop\\1.xlsx', '销项发票信息', usecols=(0, 2, 6, 7))

data.set_index('发票状态', inplace=True)
data = data.drop(labels='作废发票', axis=0)
sale.set_index('发票状态', inplace=True)
if '作废发票' in sale.index.to_list():
    sale = sale.drop(labels='作废发票', axis=0)

data.set_index('企业代号', inplace=True)
sale.set_index('企业代号', inplace=True)


def search_t(data_f, l1, l2):
    for i in data_f.index.unique():
        l1.append(i)
        data_1 = data_f.loc[i]
        b = 0
        print(data_1)
        if type(data_1) == pd.Series:
            if data_1.loc['价税合计'] < 0:
                l2.append(1)
            else:
                l2.append(0)
        else:
            for j in data_1.loc[:, '价税合计']:
                if j < 0:
                    b += 1
            l2.append(b / len(data_1))


l_1 = []
l_2 = []
search_t(data, l_1, l_2)
print(l_1)
print(l_2)

data_out = pd.DataFrame({
    '企业代号': l_1,
    '进项负单比': l_2,
})

print(data_out)

l_3 = []
search_t(sale, l_1, l_3)
ser = pd.Series(l_3)
data_out['销项负单比'] = ser

print(data_out)
data_out.to_excel('C:\\Users\\10049\\Desktop\\建模文件\\f1负单比.xlsx')