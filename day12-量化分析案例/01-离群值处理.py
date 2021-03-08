import numpy as np


# 3sigma原则处理离群值
def three_sigma(data):
    """
    基于3sigma原则的离群值处理
    :param data: 需要处理的数据
    :return: 处理之后的数据
    """
    # 上限
    up = data.mean() + 3 * data.std()
    # 下限
    low = data.mean() - 3 * data.std()

    # 超过上限 变为上限，超过下限变为下限
    data = np.where(data > up, up, data)
    data = np.where(data < low, low, data)

    return data
