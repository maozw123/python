import matplotlib.pyplot as plt
import numpy as np

# 1、创建画布
plt.figure()
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
data = np.random.uniform(low=150.0, high=195.0, size=33)
height = np.array([float("%.1f" % i) for i in data])
print(data)
print("height:\n", height)

# 绘制直方图
# bins 传单个值，默认系统分组
# plt.hist(height, bins=5, color="pink", edgecolor="b")
# 自定义分组
# bins = [150, 160, 170, 180, 190, 200]
# plt.hist(height, bins=bins, color="pink", edgecolor="b")
# 先确定分组个数
group_num = 5
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
# plt.hist(height)

# 增加刻度
plt.xticks(bins)

# 直方图不设置图例
# 设置横轴名称
plt.xlabel("身高（cm）")
# 纵轴名称
plt.ylabel("人数（个）")

# 增加标题
plt.title("身高分布直方图")

yticks = np.arange(0, 15)
# 修改纵轴刻度
plt.yticks(yticks)

# 增加网格曲线
# axis 指定只开y轴的网格曲线
#
plt.grid(True,axis="y",alpha=0.2)
# 3、图形展示
plt.show()


# 某公司 员工的薪资水平 在[3500,35000] 之间，而且公司共有55个人
# 让大家 自己自定分组，来查看大部分员工的薪水水平，来给公司做薪水指导。