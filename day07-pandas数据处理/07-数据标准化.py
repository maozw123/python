import pandas as pd
import numpy as np


# 标准化----去除量级的影响

# 3种方式
# （1）离差标准化
# 将数据做线性变化，将数据映射到【0,1】范围内，
# x = (x - min) / (max - min)
# 过大或者过小的异常值都会对结果产生影响
# 容易受到异常值影响
def max_min_sca(data):
    """
    借助离差标准化 来标准化数据
    :param data: 原数据
    :return: 标准化之后的数据
    """
    data = (data - data.min()) / (data.max() - data.min())

    return data


# （2）标准差标准化
# 借助 均值与标准差 对数据进行转换
# x = (x- mean) / std
def stand_sca(data):
    """
    标准差标准化
    :param data:原数据
    :return: 标准差之后的数据
    """
    data = (data - data.mean()) / data.std()

    return data


# 10000个【10,20】  10000----均值影响不大，标准差影响不大
# 不容易受到异常值影响


# （3）小数定标标准化
# 通过移动小数位数来把数据转化到【-1,1】之间---数据分布规律不变
# x = x /10^k
# k ----->   向上取整（log10(|x|.max())）
def desc_sca(data):
    """
    小数定标标准化数据
    :param data: 原数据
    :return: 标准化之后的数据
    """
    data = data / (10 ** int(np.ceil(np.log10(data.abs().max()))))
    return  data


# 验证：
detail = pd.read_excel("./meal_order_detail.xlsx")

print("detail 的列索引：\n", detail.columns)
# print("detail 的形状：\n", detail.shape)
print("未标准化之前：\n", detail.loc[:, "amounts"])
print("最大值与最小值：\n", detail.loc[:, "amounts"].max(), detail.loc[:, "amounts"].min())
# print("标准化之后\n", max_min_sca(detail.loc[:, "amounts"]))
# print("标准化之后\n", stand_sca(detail.loc[:, "amounts"]))
print("标准化之后\n", desc_sca(detail.loc[:, "amounts"]))
