import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_res(res):
    """
    结果展示
    :param res: 分组之后的统计结果
    :return: None
    """
    # 可视化 坏账人的占比（饼图）
    plt.figure(figsize=(20, 8))
    # 可以通过修改RC参数来让其支持中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # 添加让其继续支持负号
    plt.rcParams['axes.unicode_minus'] = False

    # 准备数据
    x = res
    # 设置名称
    labels = res.index
    # 绘制饼图
    plt.pie(x, labels=labels, autopct="%.2f%%")

    # 椭圆变成圆形
    plt.axis("equal")

    # 标题
    plt.title("年龄与坏账占比饼图")
    # 增加图例
    plt.legend(labels)
    #
    plt.show()


def box_analysis(data):
    """
    利用箱线图进行处理离群值
    :param data: 需要处理的数据
    :return: 处理之后的数据
    """
    # 计算上四分位数
    qu = data.quantile(q=0.75)
    # 计算下四分位数
    ql = data.quantile(q=0.25)
    # 计算四分位数间距
    iqr = qu - ql
    # 上限
    high = qu + 1.5 * iqr

    # 如果大于上限则变为上限，否则还是原来的数据
    # 如果参数1 的条件满足，则执行参数2，否则执行参数3
    data = np.where(data > high, high, data)

    return data


# 加载数据
data = pd.read_csv("./loan.csv", encoding="ansi")
print("data:\n", data)
print("data 的列索引名称：\n", data.columns)

#  按照年龄进行分组 查看坏账率
# 筛选特征值
data = data.loc[:, ["好坏客户", "年龄"]]
print("data:\n", data)
print("data 的列索引名称：\n", data.columns)

# 检测缺失值
res_null = pd.isnull(data).sum()
print("缺失值检测结果：\n", res_null)
print("*" * 100)

# 检测异常值----无异常值，但是上限存在离群值
# 使用box_analysis来将超过上限的数据拉回到上限
data.loc[:, "年龄"] = box_analysis(data.loc[:, "年龄"])
#
# # 标准化？？？---暂时不需要
#
# # 检测年龄去重之后的具体的个数
# # res_drop_dup = data.drop_duplicates(subset="年龄",keep="first",inplace=False)
# #
# # print(res_drop_dup.shape)
# # 等宽分组  ----结果效果不好
# group_num = int(input("请输入要拆分的组数："))
# # 计算极差
# ptp = data.loc[:, "年龄"].ptp()
#
# # 确定步长
# step = int(np.ceil(ptp / group_num))
#
# # 获取年龄的最大值 最小值
#
# print("年龄的最小值、最大值为：\n",data.loc[:, "年龄"].min(), data.loc[:, "年龄"].max())
# print("*" * 100)
# # 构建年龄分组的端点
# bins = np.arange(data.loc[:, "年龄"].min(), data.loc[:, "年龄"].max() + step, step)
#
#
# 等频分组
group_num = int(input("请输入要拆分的组数："))

# 设置年龄端点
bins = data.loc[:, "年龄"].quantile(q=np.arange(0, 1 + 1 / group_num, 1 / group_num))
#
# # 对年龄年龄进行离散化
data.loc[:, "年龄"] = pd.cut(data.loc[:, "年龄"], bins=bins, include_lowest=True)

# 查看一下分组结果以及各个组的坏用户的人数
# res_counts = pd.value_counts(data.loc[:, "年龄"])
#
# print(res_counts)
# print("*" * 100)

# 按照年龄 进行分组统计 坏用户的数量
res_sum = data.groupby(by="年龄")["好坏客户"].sum()
print(res_sum)

show_res(res_sum)





