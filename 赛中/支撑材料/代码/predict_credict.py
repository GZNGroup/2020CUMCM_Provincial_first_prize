# 违规预测
import pandas as pd
import math

data = pd.read_excel('C:\\Users\\10049\\Desktop\\建模文件\\预测违约率.xlsx')

input_1 = -6.920
output_1 = -2.405
average_ra = -0.001
average_mon = -0.000
average_number = -0.125
input_2 = 1.769
output_2 = 5.587

data.loc[:, '违约预测'] = input_1 * data['进项负单比'] + output_1 * data['销项负单比'] + average_ra * data['月均利润率'] + \
                      average_number * data['月均订单数'] + input_2 * data['进项发票作废比'] + output_2 * data['销项发票作废比'] - 0.511

# average_num = -0.127
# out_put = 5.902
#
# data.loc[:, '违约预测'] = average_num * data['月均订单数'] + out_put * data['销项发票作废比'] - 0.808
l1 = []
l2 = []
for i in data['违约预测']:
    p = math.exp(i) / (1 + math.exp(i))
    l1.append(p)
    if p > 1 / 17:
        l2.append("D")
    elif p > 1 / 38:
        l2.append('C')
    elif p > 1 / 10000:
        l2.append('B')
    else:
        l2.append('A')

data.loc[:, '违规概率'] = pd.Series(l1)
data.loc[:, '预测信誉评级'] = pd.Series(l2)
print(data)

data.to_excel('C:\\Users\\10049\\Desktop\\建模文件\\f1预测违约.xlsx')
