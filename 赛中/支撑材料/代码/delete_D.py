# 剔除信誉D级企业
import pandas as pd

data = pd.read_excel('C:\\Users\\10049\\Desktop\\1.xlsx', '销项发票信息', usecols=(0, 7))
D = pd.read_excel('C:\\Users\\10049\\Desktop\\1.xlsx', '企业信息', usecols=(0, 2))

delete = []
for i in range(123):
    if D.iloc[i, 1] == 'D':
        delete.append(i)
D = D.drop(labels=delete, axis=0)
print(D)
D.set_index('企业代号', inplace=True)
data_1 = data.value_counts()

list_1 = []
list_2 = []
for i in D.index.to_list():
    print(i)
    list_1.append(i)
    E = data_1.loc[i]
    print(E)
    if len(E) > 1:
        list_2.append(E.iloc[1] / (E.iloc[0] + E.iloc[1]))
    else:
        list_2.append(0 / E.iloc[0])

S1 = pd.Series(list_2, index=list_1)
print(S1)
S1.to_excel('C:\\Users\\10049\\Desktop\\2.xlsx')