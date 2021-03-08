import matplotlib.pyplot as plt
import numpy as np


# 构建数据
def build_data():
    """
    构建数据
    :return: 数据
    """
    # 加载数据 --返回对象
    res = np.load("./国民经济核算季度数据.npz", allow_pickle=True)
    # 从对象中获取具体的数组
    columns = res["columns"]
    values = res["values"]
    # 打印
    print("columns:\n", columns)
    print("values:\n", values)
    # 返回数据
    return columns, values


def show_data(columns, values):
    """
    绘制图形
    :param columns: 列名
    :param values: 数据
    :return: Nonoe
    """
    # 1、创建画布--返回画布对象
    # 调整画布大小
    fig = plt.figure(figsize=(20, 12), dpi=120)
    # 支持中文与负号
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False

    # 调整子图间距
    plt.subplots_adjust(hspace=0.3)
    # 添加子图 1
    fig.add_subplot(2, 1, 1)
    # 构建数据
    x = (list(values[:, 3]), list(values[:, 4]), list(values[:, 5]))
    # 构建标签
    labels = [tmp[:4] for tmp in columns[3:6]]
    # 绘制图形
    plt.boxplot(x, notch=True, labels=labels, meanline=True, showmeans=True)
    # 设置标题
    plt.title("2000-2017年各个产业生产总值箱线图")
    # 设置横轴名称
    plt.xlabel("产业")
    # 纵轴名称
    plt.ylabel("生产总值（亿元）")

    # 添加子图2
    fig.add_subplot(2, 1, 2)
    # 构建数据
    x = (list(values[:, 6]), list(values[:, 7]), list(values[:, 8]), list(values[:, 9]), list(values[:, 10]),
         list(values[:, 11]), list(values[:, 12]), list(values[:, 13]), list(values[:, 14]))
    # 构建标签
    labels = [tmp[:2] for tmp in columns[6:]]
    # 绘制图形
    plt.boxplot(x, notch=True, labels=labels, meanline=True, showmeans=True)
    plt.title("2000-2017年各个行业生产总值箱线图")
    plt.xlabel("行业")
    plt.ylabel("生产总值（亿元）")

    plt.savefig("./2000-2017年各个产业、行业生产总值箱线子图.png")
    plt.show()


def main():
    # 1、加载数据
    columns, values = build_data()
    # 2、绘制图形
    show_data(columns, values)


if __name__ == '__main__':
    main()
