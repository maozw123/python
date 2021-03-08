import pandas as pd


# 异常值---远离正常值范围的 错误值
# 异常值------删掉

# 异常值判断---3sigma  箱线图分析

# 3sigma  借助标准正态部分得到的规律----99.73% 都在(u -3a,u+3a)之间，超过这个范围的数据认为是异常的
def three_sigma(data):
    """
    进行3sigma 异常值剔除
    :param data: 原数据--series
    :return: bool数组
    """
    # 上限
    up = data.mean() + 3 * data.std()
    # 下限
    low = data.mean() - 3 * data.std()

    # 在上限与下限之间的数据 是正常的
    bool_index = (data < up) & (data > low)

    return bool_index


def box_analysis(data):
    """
    箱线图分析去除异常值
    :param data: 原数据---series
    :return: bool数组
    """
    # 上四分位数
    qu = data.quantile(q=0.75)
    # 下四分位数
    ql = data.quantile(q=0.25)
    # 计算四分位间距
    iqr = qu - ql

    # 上限
    up = qu + 1.5 * iqr
    # 下限
    low = ql - 1.5 * iqr

    bool_index = (data < up) & (data > low)

    return bool_index

# 验证---加载detail
detail = pd.read_excel("./meal_order_detail.xlsx")

print("detail 的列索引：\n", detail.columns)
print("detail 的形状：\n", detail.shape)

# 对amounts 列进行异常值处理
# bool_index = three_sigma(detail.loc[:, "amounts"])
bool_index = box_analysis(detail.loc[:, "amounts"])

# 获取异常值处理之后的结果
detail = detail.loc[bool_index,:]
print("异常值处理之后的结果：\n",detail.shape)
