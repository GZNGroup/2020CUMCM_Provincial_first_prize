# 最终策略
import numpy as np
import pandas as pd

data = pd.read_excel('C:\\Users\\10049\\Desktop\\建模文件\\risk3.xlsx', 'Sheet1')
# 最终贷款策略计算
data.set_index('企业代号', inplace=True)

max_xa = 0.047

max_xb = 0.0518

max_xc = 0.0538

for i in data.index:
    cred = data.loc[i, 'risk']
    s = data['risk'].sum()
    if data.loc[i, '信誉评级'] == 'A':
        data.loc[i, '信赖程度'] = (1 - cred)/s
        data.loc[i, '贷款利率'] = max_xa
    if data.loc[i, '信誉评级'] == 'B':
        data.loc[i, '信赖程度'] = (1 - cred)/s
        data.loc[i, '贷款利率'] = max_xb
    if data.loc[i, '信誉评级'] == 'C':
        data.loc[i, '信赖程度'] = (1 - cred)/s
        data.loc[i, '贷款利率'] = max_xc
    if data.loc[i, '信誉评级'] == 'D':
        data.loc[i, '信赖程度'] = 0


print(data.loc[:, '信赖程度'])

print(data)
data.to_excel('C:\\Users\\10049\\Desktop\\建模文件\\问题三最终结果.xlsx', 'Sheet1')
