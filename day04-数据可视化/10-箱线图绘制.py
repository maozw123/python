# 箱线图----利用最小值、下四分位数、中位数、上四分位数、最大值来描述数据
# 查看数据是否对称、是否离散、查看分布情况

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
    # 准备绘制箱子的真实数据
    # 注意：绘制箱线图的时候每一个箱子的数据必须是单个数据
    x = (values[:, 3], values[:, 4], values[:, 5])
    # notch ---是否开缺口
    # vert  箱子的朝向
    # labels 箱子的标签
    labels = [tmp[:4] for tmp in columns[3:6]]
    # meanline  均线 必须和showmeans 共同使用才能 显示均线
    plt.boxplot(x, notch=True, labels=labels, meanline=True, showmeans=True)

    # 增加标题
    plt.title("2000-2017年各个产业生产总值箱线图")
    # 增加横轴名称
    plt.xlabel("产业")
    # 增加纵轴名称
    plt.ylabel("生产总值（亿元）")
    # 保存图片
    plt.savefig("./2000-2017年各个产业生产总值箱线图.png")
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
