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

# 加载数据
data = pd.read_csv("./loan.csv", encoding="ansi")
print("data:\n", data)
print("data 的列索引名称：\n", data.columns)

# 按照家庭人口数量来查看坏账率
# 筛选特征
data = data.loc[:, ["好坏客户", "家属数量"]]

# 检测缺失值
res_null = pd.isnull(data).sum()
print("检测缺失值结果：\n", res_null)
print("*" * 100)

# 填充缺失值
# 按照下一个邻居来填充
data.loc[:, "家属数量"].fillna(method="bfill", inplace=True)

res_null = pd.isnull(data).sum()
print("检测缺失值结果：\n", res_null)
print("*" * 100)
# 检测家属数量去重之后的结果
# res_drop_dup = data.drop_duplicates(subset="家属数量",keep="first",inplace=False)
# print(res_drop_dup.shape)
# # 异常值---没有异常值
# # 标准化----不需要
# # # 等宽法 --不合适
# # group_num = int(input("请输入要拆分的组数："))
# # # # 计算极差
# # ptp = data.loc[:, "家属数量"].ptp()
# # #
# # # # 确定步长
# # step = int(np.ceil(ptp / group_num))
# # #
# # # # 获取家属数量的最大值 最小值
# # print("家属数量的最小值、最大值为：\n",data.loc[:, "家属数量"].min(), data.loc[:, "家属数量"].max())
# # print("*" * 100)
# # # # 构建年龄分组的端点
# # bins = np.arange(data.loc[:, "家属数量"].min(), data.loc[:, "家属数量"].max() + step, step)
#
#
# # 等频法---不合适 甚至还报错
# # group_num = int(input("请输入要拆分的组数："))
# #
# # # 设置年龄端点
# # bins = data.loc[:, "家属数量"].quantile(q=np.arange(0, 1 + 1 / group_num, 1 / group_num))
#
#
# 自定义宽度
bins = [0, 1, 2, 3, 4, 20]
# 离散化
data.loc[:, "家属数量"] = pd.cut(data.loc[:, "家属数量"], bins=bins, include_lowest=True)

# print()
# 按照家属数量统计坏账 中坏用户数量
res = data.groupby(by="家属数量")["好坏客户"].sum()
# res = data.groupby(by="家属数量")["好坏客户"].count()

print(res)

show_res(res)