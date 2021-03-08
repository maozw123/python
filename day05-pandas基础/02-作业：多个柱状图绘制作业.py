import matplotlib.pyplot as plt
import numpy as np


def build_data():
    """
    构建数据
    :return:数据
    """
    res = np.load("./国民经济核算季度数据.npz", allow_pickle=True)
    columns = res["columns"]
    values = res["values"]
    print(columns)
    print(values)
    return columns, values


def plot_data(columns, values, min_i, max_i, title, xlabel, ylabel, legend_index, year_index):
    """
    :param columns: 列名
    :param min_i: 最小的列下标
    :param max_i: 最大的列下标
    :param title: 标题
    :param xlabel: 横轴标题
    :param ylabel: 纵轴标题
    :param legend_index: 图例
    :param values:数据
    :param year_index:年份行数下标
    :return:
    """
    # 设置横轴
    x = np.arange(1, max_i - min_i + 2)

    # 设置纵轴
    height = values[year_index, min_i:(max_i + 1)]

    plt.bar(x, height, width=0.5)

    # 进行标注
    for i, j in zip(x, height):
        plt.text(i, j + 100, "%.2f亿元" % j, horizontalalignment='center')
    #
    # 增加标题
    plt.title(title)
    #
    # 设置横纵轴的标题
    plt.xlabel(xlabel)

    plt.ylabel(ylabel)
    #
    # 修改刻度
    xticks = [tmp[:legend_index] for tmp in columns[min_i:max_i + 1]]

    # 设置刻度
    plt.xticks(x, xticks)


def show_data(columns, values):
    """
    结果展示
    :param columns: 列名
    :param values: 数据
    :return: None
    """
    # 1、创建画布
    fig = plt.figure(figsize=(20, 12), dpi=120)
    # 支持中文与负号
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False

    # 添加子图
    fig.add_subplot(2, 2, 1)
    title = "2000年第一季度各产业生产总值柱状图"
    xlabel = "产业"
    ylable = "生产总值（亿元）"
    plot_data(columns, values, 3, 5, title, xlabel, ylable, legend_index=4, year_index=0)

    fig.add_subplot(2, 2, 2)
    title = "2017年第一季度各产业生产总值柱状图"
    plot_data(columns, values, 3, 5, title, xlabel, ylable, legend_index=4, year_index=-1)

    fig.add_subplot(2, 2, 3)
    title = "2000年第一季度各行业生产总值柱状图"
    xlabel = "行业"
    ylable = "生产总值（亿元）"
    plot_data(columns, values, 6, 14, title, xlabel, ylable, legend_index=2, year_index=0)

    fig.add_subplot(2, 2, 4)
    title = "2017年第一季度各行业生产总值柱状图"
    plot_data(columns, values, 6, 14, title, xlabel, ylable, legend_index=2, year_index=-1)

    # 保存图片
    plt.savefig("./2000、2017年第一季度各产业、行业生产总值柱状图.png")

    plt.show()


def main():
    """
    主函数
    :return:
    """
    # 构建数据
    columns, values = build_data()

    # 展示结果
    show_data(columns, values)


if __name__ == '__main__':
    main()
