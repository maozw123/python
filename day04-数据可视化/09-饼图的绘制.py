# 饼图的应用场景：
# 用于部分与部分的对比，部分与整体的关系对比


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
    绘制饼图
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
    # 准备数据
    x = values[-1, 3:6]
    print("x:\n", x)

    # explode --各部分距离圆心的半径，也可以理解为各部分之间的缝隙
    explode = (0.01, 0.02, 0.03)
    # labels  各个部分的名称
    labels = [tmp[:4] for tmp in columns[3:6]]
    # colors 各部分的颜色
    colors = ["r", "g", "b"]
    # autopct 占比输出
    autopct = "%.2f%%"
    # pctdistance 占比输出的位置
    # labeldistance labels 的位置
    # shadow 阴影
    # radius 饼图的半径
    plt.pie(x, explode=explode, labels=labels, colors=colors, autopct=autopct, shadow=True,labeldistance=1.1)

    # 将椭圆的饼子 变成圆形
    plt.axis("equal")

    # 设置图例
    plt.legend(labels)

    # 增加标题名称
    plt.title("2017年各产业生产总值占比饼图")

    # 保存图片
    plt.savefig("./2017年各产业生产总值占比饼图.png")
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
