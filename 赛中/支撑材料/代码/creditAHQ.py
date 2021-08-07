import pandas as pd
import numpy as np

data = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\for_credit2.xlsx', usecols=(0, 10, 11, 12))
power=pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\信誉影响因素权重.xls', 'AHP层次分析结果', usecols=(2,))

output=data['企业代号'].to_frame()
output['credit'] = np.mat(data.iloc[:, 1:])*np.mat(power['权重值'].to_frame())
output.to_excel('C:\\Users\\HPDC0006\\Desktop\\结果表格\\credit2.xlsx', index=None)
