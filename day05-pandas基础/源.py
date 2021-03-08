'''
将给定的数据data.npz加载出来，然后根据自己掌握的的绘图知识，
绘制出各个的产品的价格随时间的走势图。（横轴刻度每个30天标注一次，倾斜45度）
'''
import matplotlib.pyplot as plt
import numpy as np

# 某公司 员工的薪资水平 在[3500,35000] 之间，而且公司共有55个人
# 让大家 自己自定分组，来查看大部分员工的薪水水平，来给公司做薪水指导。

def add_data():
    res = np.load("./data.npz", allow_pickle=True)
    # for tmp in res:
    #     print(tmp)
    columns = res["columns"]
    values = res["values"]

    print("columns:\n", columns)
    print("values:\n", values)
    return columns,values

def show_data(columns,values):
    # 1、创建画布
    fig = plt.figure(figsize=(20, 12))
    # 默认不支持中文
    # 修改RC参数，来让其支持中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    # 2、绘制图形
    # 绘制直方图---
    # 横轴----真实数据的区间
    # 纵轴---落在各个区间内的数量
    # 构建数据
    # 班级同学身高的分布直方图

    fig.add_subplot(2, 2, 1)

    data = np.random.uniform(low=3500, high=35000, size=55)
    height = np.array([float("%.1f" % i) for i in data])
    print(data)
    print("height:\n", height)

    group_num = 6
    # 先计算最大值与最小值差距
    ptp = height.max() - height.min()

    # 确定每一组的组距
    step = int(np.ceil(ptp / group_num))

    print("min:\n", height.min())
    print("max:\n", height.max())
    print(step)

    bins = np.arange(height.min(), height.max() + step, step)
    print("bins:\n", bins)

    plt.hist(height, bins=bins, color="pink", edgecolor="b")

    plt.xlabel("工资（元）")
    plt.ylabel("人数（个）")
    plt.title("员工工资分布直方图")
    plt.xticks(bins)
    yticks = np.arange(0, 15)
    plt.yticks(yticks)

    # 增加网格曲线
    # axis 指定只开y轴的网格曲线
    plt.grid(True, axis="y", alpha=0.1)


    fig.add_subplot(2, 2, 2)
    x=np.arange(1,10,1)
    print(x)
    y=values[-1,6:]
    plt.bar(x,y,width=0.5, color=["b",'pink','y','g','r',])
    xticks=[i[:2] for i in columns[6:]]
    plt.xticks(x,xticks)
    plt.xlabel('行业')
    plt.ylabel('生产总值（亿元）')
    plt.title('2017年第一季度国民生产总值行业构成分布柱状图')
    for i, j in zip(x,y):
        plt.text(i, j, "%.2f亿元" % j, horizontalalignment='center', verticalalignment='bottom', )

    # 2017年各产业生产总值饼图
    fig.add_subplot(2, 2, 3)
    x = values[-1, 3:6]
    print("x:\n", x)

    # explode --各部分距离圆心的半径，也可以理解为各部分之间的缝隙
    explode = (0.001, 0.002, 0.003)
    # labels  各个部分的名称
    labels = [tmp[:4] for tmp in columns[3:6]]
    # colors 各部分的颜色
    colors = ["r", "y", "b"]
    # autopct 占比输出
    autopct = "%.2f%%"
    # pctdistance 占比输出的位置
    # labeldistance---- labels 的位置
    # shadow 阴影
    # radius 饼图的半径
    # plt.pie(x, explode=explode, labels=labels, colors=colors, autopct=autopct, shadow=True, labeldistance=1.05)
    plt.pie(x, explode=explode, labels=labels, colors=colors, autopct=autopct, labeldistance=1.05)

    # 椭圆变园
    plt.axis("equal")
    plt.legend(labels, loc=2)

    # 增加标题名称
    plt.title("2017年各产业生产总值占比饼图")

    fig.add_subplot(2, 2, 4)
    # 箱线图的绘制
    x = (values[:, 6], values[:, 7], values[:, 8], values[:, 9], values[:, 10], values[:, 11], values[:, 12], values[:, 13],
         values[:, 14])
    labels = [tmp[:2] for tmp in columns[6:]]
    plt.boxplot(x,labels=labels,notch=True, meanline=True, showmeans=True,)
    plt.title('2000-2017各行业国民生产总值箱线图')
    plt.xlabel('行业')
    plt.ylabel('生产总值（亿元）')

    plt.savefig("./柱状图直方图饼图箱线图练习.png")
    # 3、图形展示
    plt.show()

if __name__ == '__main__':
    columns,values=add_data()
    show_data(columns,values)