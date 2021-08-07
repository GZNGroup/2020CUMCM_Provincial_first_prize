import pandas as pd

data = pd.read_excel('E:\\1.xlsx', '进项发票信息', usecols=(0, 7))
print(data.iloc[0, 1])

name = data.iloc[0, 0]
all = 0
unuseful = 0
rate=0
for x in range(len(data)):
    if name == data.iloc[x, 0]:
        all += 1
        if data.iloc[x, 1] == "作废发票":
            unuseful += 1
    else:
        rate=unuseful/all
        
        all=0
        unuseful=0
        name=data.iloc[x, 0]
    rate=unuseful/all


