import matplotlib.pyplot as plt
import numpy as np

res = np.load('./国民经济核算季度数据.npz')
print(res)
for tem in res:
    print(tem)

columns = res['columns']
values = res['values']
print('columns:\n', res['columns'])
print('values:\n', res['values'])

# 1、创建画布
fig = plt.figure()
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# 2、绘图
# 散点图的坐标系元素 是 点 ，点的要素---坐标
# 构建横纵坐标
x = values[:, 0]
y = values[:, 3]
y1 = values[:, 6]
y2 = values[:, 4]

# 绘图
# s 点的大小，可以是单个值，可以是array
# c 点的颜色，可以是单个颜色，也可以颜色array
#  marker ---点的类型
# plt.scatter(x, y, s=30, c="r", marker="*", alpha=1)
s = [7, 2, 30, 15, 20, 25, 50]
# s = [2, 25, 50] # 如果点的数量大于 点的大小的列表，那么会循环去列表拿值
c = ["r", "g", 'b', "y", "pink", "m", "k"]
# marker_list = ["*", "o", "*", "*", "*", "*", "*"]
#
# 点的样式marker必须单个的值
# alpha  透明度 1  完全实体， 0 --完全透明  越大越凝实，越小越透明
# plt.scatter(x, y1, s=s, c=c, marker="*", alpha=1)
fig.add_subplot(2, 1, 1)
# plt.scatter(x, y, s=s, c=c, marker="o", alpha=0.8)
plt.scatter(x, y, s=10)
plt.title("2000-2017年各产业季度生产总值走势图")
xticks = values[:, 1]
plt.xticks(x[::4], xticks[::4], rotation=45, horizontalalignment="center")
# scatter x 与y 元素必须是一致 的才能绘制
# plt.plot(x,y) # 可以的


fig.add_subplot(2, 1, 2)
plt.scatter(x, y2, s=15)
# 3、绘图展示
plt.show()
