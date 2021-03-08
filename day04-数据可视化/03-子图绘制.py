import matplotlib.pyplot as plt
import numpy as np

# 加载数据
res = np.load("./国民经济核算季度数据.npz", allow_pickle=True)

columns = res["columns"]
values = res["values"]

print("columns:\n", columns)
print("values:\n", values)

# 绘图三部曲
# 1、创建画布，并返回画布对象
fig = plt.figure(figsize=(20,10),dpi=120)
# 增加RC参数
# 默认不支持中文
# 修改RC参数，来让其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 给画布里面添加 多个坐标系
# 参数1  子图的行数
# 参数2  子图的列数
# 参数3  第几个子图
fig.add_subplot(2, 1, 1)

# 2、绘图
# 横轴---时间（直接绘制的时候，不允许使用中文）---先用序号来代替时间
# 纵轴----生产总值

# 自己生成
x = np.arange(1, values.shape[0] + 1)
print("x:\n", x)

y1 = values[:, 3]
y2 = values[:, 4]
y3 = values[:, 5]

print("y1:\n", y1)
print("y2:\n", y2)
print("y3:\n", y3)

# 绘图---自己可以构建各种rc来区别点线
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# 增加标题
plt.title("2000-2017年各产业、行业季度生产总值走势图")

legend = [tmp[:4] for tmp in columns[3:6]]
# 增加图例
plt.legend(legend, loc=2)

# # 增加横轴名称
# plt.xlabel("季度")

# 增加纵轴名称
plt.ylabel("生产总值（亿元）")



# 第二个子图
fig.add_subplot(2, 1, 2)
x = values[:, 0]
y1 = values[:, 6]
y2 = values[:, 7]
y3 = values[:, 8]
y4 = values[:, 9]
y5 = values[:, 10]
y6 = values[:, 11]
y7 = values[:, 12]
y8 = values[:, 13]
y9 = values[:, 14]

# 绘制 图形
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.plot(x,y6)
plt.plot(x,y7)
plt.plot(x,y8)
plt.plot(x,y9)


# 纵轴名称
plt.ylabel("生产总值（亿元）")
# 横轴名称
plt.xlabel("季度")

# 设置横轴刻度

xticks = values[:, 1]
# plt.xticks(x, xticks, rotation=75)
plt.xticks(x[::4], xticks[::4], rotation=45, horizontalalignment="center")

legend = [tmp[:2] for tmp in columns[6:]]
# 增加图例
plt.legend(legend,loc=2)

# 保存图片
plt.savefig("./2000-2017年各产业、行业季度生产总值走势图.png")


# 3、图形展示
plt.show()
