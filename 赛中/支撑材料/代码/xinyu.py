# -*- encoding=utf-8 -*-

import numpy as np
import pandas as pd


# 自定义归一化函数

def autoNorm(data1):
    """
    :param data: 列表
    :return: 归一化列表
    """
    arr = np.asarray(data1)
    norm_list = []
    for x in arr:
        x = round(float(x - np.min(arr)) / ((np.max(arr) - np.min(arr)) + 0.001), 4)
        norm_list.append(x)

    return norm_list


# 自定义热度值计算函数

def credit(usefulData):
    """
    :param usefulData:数据框
    :return: 热度值分数
    """

    #  求相关列均值与标准差

    context_train_mean = usefulData.mean(axis=0)

    context_train_std = usefulData.std(ddof=0)

    #  求变异系数

    context_train_cof_var = context_train_std / context_train_mean

    #  对变异系数求和

    sum_context_train_cof_var = context_train_cof_var.sum()

    #  得出权重

    context_train_wi = context_train_cof_var / sum_context_train_cof_var

    #  将权重转换为矩阵

    cof_var = np.mat(context_train_wi)

    #  将数据框转换为矩阵
    usefulData = np.mat(usefulData)

    #  权重跟自变量相乘
    last_hot_matrix = usefulData * cof_var.T
    last_hot_matrix = pd.DataFrame(last_hot_matrix.T)

    #  累加求和得到总分
    last_hot_score = list(last_hot_matrix.apply(sum))

    #  max-min 归一化

    last_hot_score_autoNorm = autoNorm(last_hot_score)

    #  部落的热度值映射成分数（0-100分）

    last_hot_score_result = [i for i in last_hot_score_autoNorm]

    return last_hot_score_result


if __name__ == '__main__':
    # 读取数据
    # context_train_data=pd.DataFrame(np.arange(24).reshape(4,6),columns=['x1','x2','x3','x4','x5','x6'])

    allData = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\for_credit.xlsx')
    data = pd.read_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\for_credit.xlsx', usecols=(3, 4, 5))

    # 调用信誉值计算函数
    result = credit(data)

    # 增加一列热度值
    output = allData['企业代号'].to_frame()
    output['信誉值'] = result
    output.to_excel('C:\\Users\\HPDC0006\\Desktop\\预处理表格\\credit.xlsx')
