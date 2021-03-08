import matplotlib.pyplot as plt
import numpy as np
# 1.创建画布
plt.figure(figsize=(20,8),dpi=120)
# 默认不支持中文,写下plt.rcParams['font.sans-serif']='SimHei'就支持中文
plt.rcParams['font.sans-serif']='SimHei'
# 负号 False支持复数
plt.rcParams['axes.unicode_minus']=False

# 2.绘画--以简单的折线图为例
# 准备横轴纵轴
# 横轴--序号
# 纵轴--温度
x=np.arange(1,8)
y_bj=np.array([12,10,8,6,-5,3,10])
y_sh=np.array([23,20,21,25,28,26,18])
# 回执折线图
plt.plot(x,y_bj,color='r', linestyle=':', linewidth=1.2, marker="*", markersize=7, markerfacecolor='b', markeredgecolor='g')
plt.plot(x,y_sh,color='y', linestyle=':', linewidth=1.2, marker="*", markersize=7, markerfacecolor='b', markeredgecolor='g')
# 注意：有的修饰可以放在绘图之前，也可以放在绘图之后，但是有的修饰必须放在绘图之后，所以为了避免不必要的麻烦，
# 修饰建议统统的放在绘图之后
plt.title('下一周北京天气走势图')

# 增加横轴名称
plt.xlabel('日期',verticalalignment='top')
# 增加纵轴名称
# ratation=0旋转角度
plt.ylabel('温度（℃）',rotation=0,horizontalalignment='right')

# loc=2 调整图例的位置，默认找出最好的位置

xticks=['周一','周二','周三','周四','周五','周六','周日']
# 修改刻度
# 修改横轴刻度
# 如果要使用中文
# 参数一 原先的刻度
# 参数二 需要替换的中文
plt.xticks(x,xticks)

yticks=np.arange(-6,34,3)
# 如果重新设置刻度
# 参数 直接设置新的刻度
plt.yticks(yticks)

plt.legend(['北京','上海'],loc=2)

# for i ,j in zip(x,y_bj):
#     plt.text(i,j+1,'%d℃'%j,horizontalalignment='center')
#
# for i ,j in zip(x,y_sh):
#     plt.text(i,j+1,'%d℃'%j,horizontalalignment='center')

plt.savefig('./下周北京，上海温度走势图')
# 3.图像展示
plt.show()