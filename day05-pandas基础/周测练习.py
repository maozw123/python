import matplotlib.pyplot as plt
import numpy as np

'''
将给定的数据data.npz加载出来，然后根据自己掌握的的绘图知识，
绘制出各个的产品的价格随时间的走势图。（横轴刻度每个30天标注一次，倾斜45度）
'''


res = np.load("./data.npz", allow_pickle=True)
for tmp in res:
    print(tmp)
col = res["col"]
val = res["val"]

print('col:\n', col)
print('val:\n', val)
# 1创建画布
fig=plt.figure(figsize=(20,20))
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 2绘图----六个子图-----
# 折线图
fig.add_subplot(2,3,1)
x=np.arange(0,366,30)
# y1=val[::30,1]
# y2=val[::30,2]
# y3=val[::30,3]
# y4=val[::30,4]
# y5=val[::30,5]
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.plot(x,y3)
# plt.plot(x,y4)
# plt.plot(x,y5)
for i in range(1,6):
    y=val[::30,i]
    plt.plot(x,y)
    # for i, j in zip(x, y):
    #     # print(i.astype(str),j,type(i.astype(str)),type(j))
    #     plt.text(i.astype(str), j , '元' % j, horizontalalignment='center')
plt.xticks(x,val[::30,0],rotation=45)
plt.legend(col[1:])
plt.title("2019年各个利润变化图")
plt.ylabel("利润(万元)")
plt.xlabel("时间")

# 散点图
fig.add_subplot(2,3,2)
x=np.arange(0,366,30)
for i in range(1,6):
    y=val[::30,i]
    plt.scatter(x,y)
plt.xticks(x,val[::30,0],rotation=45)
yticks=np.arange(0,3000,50)
plt.yticks(yticks)
plt.legend(col[1:])
plt.title("2019年各个利润变化图")
plt.ylabel("利润(万元)")
plt.xlabel("时间")
# 饼图
fig.add_subplot(2,3,3)
x=val[-1,1:]
autopct = "%.2f%%"
labels = [tmp for tmp in col[1:]]
plt.pie(x,autopct=autopct,labels=labels)
plt.legend(labels)

# 箱线图
fig.add_subplot(2,3,4)

# x = (val[:, 1].astype(float), val[:, 2].astype(float), val[:, 3].astype(float),val[:, 4].astype(float),val[:, 5].astype(float))
x = (val[:, 1])
print('*'*100)
print(x)
# notch ---是否开缺口
# vert  箱子的朝向
# labels 箱子的标签
labels = [tmp for tmp in col[1:]]
print(labels)
# meanline  均线 必须和showmeans 共同使用才能 显示均线
plt.boxplot(x.astype(float))
# fig.add_subplot(2,3,5)
# fig.add_subplot(2,3,6)

# 3展示
plt.show()