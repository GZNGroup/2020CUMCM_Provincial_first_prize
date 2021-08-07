import numpy as np
import pandas as pd

data = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\for_power3.xlsx', usecols=(0, 1, 2, 4))
power = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\实力影响因素权重.xls', 'AHP层次分析结果', usecols=(2,))

output = data['企业代号'].to_frame()
output['power'] = np.mat(data.iloc[:, 1:]) * np.mat(power['权重值'].to_frame())
output.to_excel('C:\\Users\\HPDC0006\\Desktop\\结果表格\\power3.xlsx', index=None)
