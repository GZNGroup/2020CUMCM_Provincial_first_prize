# 贷款额度检查
import pandas as pd

data = pd.read_excel('C:\\Users\\10049\\Desktop\\建模文件\\问题三最终结果.xlsx')

data['贷款额度(万元)'] = data['信赖程度'] * 10000
if data['贷款额度(万元)'].max() > 100:
    print('存在贷款额度超额情况')
for i in data['贷款额度(万元)']:
    if i == 0:
        continue
    if i < 10 :
        print('存在贷款额度不足')
data.to_excel('C:\\Users\\10049\\Desktop\\建模文件\\问题三最终结果.xlsx')