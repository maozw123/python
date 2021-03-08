import matplotlib.pyplot as plt
import numpy as np

# 加载数据
res = np.load("./国民经济核算季度数据.npz", allow_pickle=True)
# for tmp in res:
#     print(tmp)
columns = res["columns"]
values = res["values"]

print("columns:\n", columns)
print("values:\n", values)

# 绘图三部曲
# 1、创建画布
plt.figure()
# 增加RC参数
# 默认不支持中文
# 修改RC参数，来让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 2、绘图
# 横轴---时间（直接绘制的时候，不允许使用中文）---先用序号来代替时间
# 纵轴----生产总值
# x = values[:, 0]
# print("x:\n", x)
# 自己生成
x = np.arange(1, values.shape[0] + 1)
print("x:\n", x)

# y1 = values[:, 3]
# y2 = values[:, 4]
# y3 = values[:, 5]
#
# print("y1:\n", y1)
# print("y2:\n", y2)
# print("y3:\n", y3)

y = values[:, 3:6]

# 绘图---自己可以构建各种rc来区别点线
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)

# 注意： 在折线图中，一个横坐标，可以匹配多个纵坐标
plt.plot(x,y)

# 增加标题
plt.title("2000-2017年各产业季度生产总值走势图")

legend = [tmp[:4] for tmp in columns[3:6]]
# 增加图例
plt.legend(legend, loc=2)

# 增加横轴名称
plt.xlabel("季度")

# 增加纵轴名称
plt.ylabel("生产总值（亿元）")

# 设置横轴刻度
#
xticks = values[:, 1]
# plt.xticks(x, xticks, rotation=75)
plt.xticks(x[::4], xticks[::4], rotation=45, horizontalalignment="center")

# 3、图形展示
plt.show()


# 趋势--->一般用于 某个产品的销量、某件东西上线人数随时间变化趋势
