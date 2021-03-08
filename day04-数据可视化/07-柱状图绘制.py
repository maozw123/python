import matplotlib.pyplot as plt
import numpy as np


# 构建数据
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

    print("columns:\n", columns)
    print("values:\n", values)
    return columns, values


def show_data(columns, values):
    """
    绘制柱状图
    :param columns: 名称
    :param values: 真实的数据
    :return: None
    """
    # 1、创建画布
    plt.figure()
    # 默认不支持中文
    # 修改RC参数，来让其支持中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    # 2、绘图
    # 绘制柱状图---
    # 横轴---各个类别
    # 纵轴---各个类别所对应的数据
    x = np.arange(1, 4, 1)
    print("x:\n", x)

    y = values[0, 3:6]
    print("y:\n", y)

    # 绘制柱状图
    # width  柱子的宽度
    # color 柱子的颜色
    plt.bar(x, y, width=0.5, color="b")

    # 增加标题
    plt.title("2000年第一季度各个产业柱状图")
    # 增加横轴名称
    plt.xlabel("产业")
    # 增加纵轴名称
    plt.ylabel("生产总值（亿元）")

    ticks = [tmp[:4] for tmp in columns[3:6]]
    # 修改横轴刻度
    plt.xticks(x, ticks)

    # 进行标注
    for i, j in zip(x, y):
        plt.text(i, j, "%.2f亿元" % j, horizontalalignment='center', verticalalignment='bottom', )

    # 保存图片
    plt.savefig("./2000年第一季度各个产业生产总值柱状图.png")
    # 3、图形展示
    plt.show()


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
