
import matplotlib.pyplot as plt
import numpy as np


res=np.load("./data.npz")
# print(type(res))
# for tem in res:
#     print(tem)
col=res["col"]
val=res["val"]
print(col)
print(val)

# 1、常见画布
fig = plt.figure(figsize=(15, 10), dpi=120)

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 2、绘图
fig.add_subplot(2,3,1)
x=np.arange(0,366)

# for i in range(1,6):
#     y= val[:,i]
#     plt.plot(x[::30], y[::30])
y=val[:,1]
# xticks = val[:,0]
# plt.xticks(x[::30], xticks[::30], rotation=45)
plt.title("2019年各个利润变化图")
plt.ylabel("利润(万元)")
plt.xlabel("时间")
# fig.add_subplot(2,3,1)

#数据读取





# 3、图形展示
plt.show()





