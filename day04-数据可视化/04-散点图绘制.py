import matplotlib.pyplot as plt
import numpy as np

# 1、创建画布
plt.figure()
# 2、绘图
# 散点图的坐标系元素 是 点 ，点的要素---坐标
# 构建横纵坐标
x = np.arange(1, 8)
y1 = np.array([12, 10, 8, 6, -5, 3, 10])
y2 = np.array([23, 20, 21, 25, 28, 26, 18])

y = np.concatenate((y1.reshape((-1, 1)), y2.reshape((-1, 1))), axis=-1)
print(y)
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
plt.scatter(x, y2, s=s, c=c, marker="o", alpha=0.8)

# scatter x 与y 元素必须是一致 的才能绘制
# plt.plot(x,y) # 可以的
# 3、绘图展示
plt.show()
