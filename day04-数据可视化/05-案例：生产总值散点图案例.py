import matplotlib.pyplot as plt
import numpy as np


def show_data(columns, values):
    """
    绘图展示
    :param columns: 名称
    :param values: 真实数据
    :return: None
    """
    # 1、创建画布
    fig = plt.figure(figsize=(20, 12), dpi=120)
    # 增加RC 参数
    # 默认不支持中文
    # 修改RC参数，来让其支持中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False

    # 调整子图的间隔
    # wspace=None,  来调整 子图之间左右的宽度
    # hspace=None # 来调整 子图之间上下的宽度
    plt.subplots_adjust(hspace=0.3)
    # 2、绘图
    # 创建子图
    fig.add_subplot(2, 1, 1)
    # 关于 各个季度产业散点图
    x = values[:, 0]
    y1 = values[:, 3]
    y2 = values[:, 4]
    y3 = values[:, 5]
    plt.scatter(x, y1)
    plt.scatter(x, y2)
    plt.scatter(x, y3)

    # 增加标题
    plt.title("2000-2017年各个产业、行业的散点图")
    # 增加纵轴名称
    plt.ylabel("生产总值（亿元）")
    legend = [tmp[:4] for tmp in columns[3:6]]
    # 增加图例
    plt.legend(legend)

    # 增加横轴名称
    plt.xlabel("季度")

    # 设置横轴刻度
    xticks = values[:, 1]
    plt.xticks(x[::4], xticks[::4], rotation=45)

    fig.add_subplot(2, 1, 2)
    # 关于 各个季度行业散点图
    y1 = values[:, 6]
    y2 = values[:, 7]
    y3 = values[:, 8]
    y4 = values[:, 9]
    y5 = values[:, 10]
    y6 = values[:, 11]
    y7 = values[:, 12]
    y8 = values[:, 13]
    y9 = values[:, 14]

    plt.scatter(x, y1)
    plt.scatter(x, y2)
    plt.scatter(x, y3)
    plt.scatter(x, y4)
    plt.scatter(x, y5)
    plt.scatter(x, y6)
    plt.scatter(x, y7)
    plt.scatter(x, y8)
    plt.scatter(x, y9)

    # 增加纵轴名称
    plt.ylabel("生产总值（亿元）")
    # 增加图例
    legend = [tmp[:2] for tmp in columns[6:]]
    plt.legend(legend, loc=2)

    # 设置横轴刻度
    xticks = values[:, 1]
    plt.xticks(x[::4], xticks[::4], rotation=45)

    # 增加横轴名称
    plt.xlabel("季度")

    # 保存图片
    plt.savefig("./2000-2017年各个产业、行业的散点图.png")

    # 3、图形展示
    plt.show()


def build_data():
    """
    构建数据
    :return:数据
    """
    # 加载数据
    res = np.load("./国民经济核算季度数据.npz", allow_pickle=True)
    # for tmp in res:
    #     print(tmp)
    columns = res["columns"]
    values = res["values"]

    # print("columns:\n", columns)
    # print("values:\n", values)
    return columns, values


def main():
    """
    主函数
    :return:None
    """
    # 1、加载数据
    columns, values = build_data()

    # 2、绘制图形
    show_data(columns, values)


if __name__ == '__main__':
    main()

# 场景一：类似于折线走势的这种散点图 也可以用来描述走势
# 场景二：可以用来描述 点与点（数据与数据）的关系
