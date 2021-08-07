import numpy as np
import pandas as pd

data = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\for_risk3.xlsx', usecols=(0, 1, 2, 3))
power = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\风险评估权重.xls', usecols=(3,))

output = data['企业代号'].to_frame()
output['risk'] = np.mat(data.iloc[:, 1:]) * np.mat(power['权重系数w'].to_frame())
output.to_excel('C:\\Users\\HPDC0006\\Desktop\\结果表格\\risk3.xlsx', index=None)