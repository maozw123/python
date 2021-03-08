import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 默认信用坏的用户用1 表示
# 默认信用好的用户用0 表示

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
    plt.title("月收入与坏账占比饼图")
    # 增加图例
    plt.legend(labels)
    #
    plt.show()

# 加载数据
data = pd.read_csv("./loan.csv", encoding="ansi")
print("data:\n", data)
print("data的列索引名称：\n", data.columns)
print("*" * 100)

# 筛选特征
data = data.loc[:, ["好坏客户", "月收入"]]
#
# 检测缺失值
res_null = pd.isnull(data).sum()
print("缺失值检测结果：\n", res_null)
#
# # 处理缺失值
# 填充法---众数填充
mode = data.loc[:, "月收入"].mode()[0]
data.loc[:, "月收入"].fillna(value=mode, inplace=True)
# print("*" * 100)
res_null = pd.isnull(data).sum()
print("缺失值检测结果：\n", res_null)
print("*" * 100)
# # 处理异常值---（假设没有异常值）
# # three_sigma  / box_analysis
#
#
# # 不需要标准化
# # 离差标准化   标准差标准化  小数定标标准化
#
# # 离散化
# # 等宽离散
# # 等频离散
# # 数据范围分布太大，选择等频离散
#
# 确定分组个数
group_num = int(input("请输入分组个数："))

# 求取月收入的分组节点
bins = data.loc[:, "月收入"].quantile(q=np.arange(0, 1 + 1 / group_num, 1 / group_num))
print(bins)
print("*" * 100)
#
data.loc[:, "月收入"] = pd.cut(data.loc[:, "月收入"], bins=bins, include_lowest=True)
#
# 按照月收入分组，统计坏账的人的个数---分组聚合
# 好用户是0
# 坏用户 1
res = data.groupby(by="月收入")["好坏客户"].sum()
#
print(res)
#
# # # 透视表
# # res = pd.pivot_table(
# #     data=data,
# #     index="月收入",
# #     values="好坏客户",
# #     aggfunc="sum"
# # )["好坏客户"]
# # print(res)
#
# # 结果展示
show_res(res)
# # 得出结论
# 收入越高，坏账率越低
