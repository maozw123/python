import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def stand_sca(data):
    """
    标准差标准化
    :param data:原数据
    :return: 标准差之后的数据
    """
    data = (data - data.mean()) / data.std()

    return data


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



def build_data():
    """
    构建原始数据
    :return: 原始数据
    """
    # 1、加载数据
    air_data = pd.read_csv("./air_data.csv", encoding="ansi")
    # print("air_data:\n", air_data)
    # print("air_data 的列索引名称:\n", air_data.columns)

    return air_data

def deal_data(air_data):
    """
    数据处理
    :param air_data:原始数据
    :return: 数据处理之后的结果
    """
    # 2、数据清洗
    # 缺失值、异常值
    # 检测缺失值
    res_null = pd.isnull(air_data).sum()
    # print("缺失值检测结果：", res_null)

    # 处理缺失值
    # （1）丢弃票价为空的记录 # SUM_YR_1  SUM_YR_2两列
    # ----可以理解保留票价不为空
    bool_index_1 = air_data.loc[:, "SUM_YR_1"].notnull()
    bool_index_2 = air_data.loc[:, "SUM_YR_2"].notnull()
    # print(bool_index_1)
    # print(bool_index_2)
    # # 个人认为 只有两列票价都不为空，票价才不为空
    bool_index = bool_index_1 & bool_index_2
    air_data = air_data.loc[bool_index, :]
    # print(air_data)
    # (2)丢弃票价为0，折扣不为0，飞行里程 > 0 的数据--->丢弃航空公司没有盈利的数据
    # 保留盈利的数据
    # 保留票价 > 0，折扣 > 0，飞行里程 > 0
    # 个人认为只要有一列票价>0,票价就>0
    bool_id_1 = air_data.loc[:, "SUM_YR_1"] > 0
    bool_id_2 = air_data.loc[:, "SUM_YR_2"] > 0
    #
    # 折扣> 0
    bool_id_3 = air_data.loc[:, "avg_discount"] > 0
    #
    # 飞行里程>0
    bool_id_4 = air_data.loc[:, "SEG_KM_SUM"] > 0
    #
    bool_id = (bool_id_1 | bool_id_2) & bool_id_3 & bool_id_4
    #
    air_data = air_data.loc[bool_id, :]
    #
    res_null = pd.isnull(air_data).sum()
    # print("缺失值检测结果：", res_null)
    #
    # 先筛选特征
    # LRFMC
    # 筛选 入会时间、窗口结束时间、最后乘坐飞机距离窗口结束的时长,乘坐飞机次数、飞行里程、折扣系数
    air_data = air_data.loc[:, ["FFP_DATE", "LOAD_TIME", "LAST_TO_END", "FLIGHT_COUNT", "SEG_KM_SUM", "avg_discount"]]

    # 构建LRFMC五个特征
    air_data.loc[:, "FFP_DATE"] = pd.to_datetime(air_data.loc[:, "FFP_DATE"])
    air_data.loc[:, "LOAD_TIME"] = pd.to_datetime(air_data.loc[:, "LOAD_TIME"])
    # 获取时间差--单位是day
    air_data.loc[:, "L_days"] = air_data.loc[:, "LOAD_TIME"] - air_data.loc[:, "FFP_DATE"]
    # 获取相差天数 的数值
    air_data.loc[:, "L_days"] = [i.days for i in air_data.loc[:, "L_days"]]
    # 获取具体的月数--即L
    air_data.loc[:, "L"] = np.ceil(air_data.loc[:, "L_days"] / 30)
    # print(air_data.loc[:, "L"])
    # 构建R --- LAST_TO_END 这个时长应该是天数
    # print(air_data.loc[:, "LAST_TO_END"])
    air_data.loc[:, "R"] = np.ceil(air_data.loc[:, "LAST_TO_END"] / 30)
    # print("air_data.loc[:, "R"]:\n",air_data.loc[:, "R"])

    air_data.loc[:, "F"] = air_data.loc[:, "FLIGHT_COUNT"]

    air_data.loc[:, "M"] = air_data.loc[:, "SEG_KM_SUM"]

    air_data.loc[:, "C"] = air_data.loc[:, "avg_discount"]

    air_data = air_data.iloc[:, -5:]
    # print("最终的数据：\n", air_data)

    # 异常值处理
    for column in air_data.columns:
        bool_ = box_analysis(air_data.loc[:, column])
        air_data = air_data.loc[bool_, :]

    # 标准化数据
    air_data = stand_sca(air_data)

    print("标准化之后的数据：\n", air_data)

    return air_data

if __name__ == '__main__':
    air_data=build_data()

    deal_data(air_data)
