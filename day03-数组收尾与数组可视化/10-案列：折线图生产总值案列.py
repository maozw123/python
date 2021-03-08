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
# x=values[0:79:4,0]
x=values[::4,0]
y=values[::4,3]
# print('y\n',y)

y_zz=values[0:79:4,2]#总值
# print(y_zz)
xticks=values[0:79:4,1]
yticks=np.arange(0,100001,20000)
# print(y)
# x=np.hsplit(values,15)[0].reshape(69)
# # print(x)
# y=np.hsplit(values,15)[4].reshape(69)
# xticks=np.hsplit(values,15)[1].reshape(69)
# xticks=np.hsplit(values,15)[1]
# print(xticks)
# # print(y)
plt.figure(figsize=(20,8),dpi=120)
# plt.plot(x,y)
plt.plot(x,y,color='r', linestyle=':', linewidth=1.2, marker="*", markersize=7, markerfacecolor='b', markeredgecolor='g')
plt.plot(x,y_zz,color='r', linestyle=':', linewidth=1.2, marker="*", markersize=7, markerfacecolor='b', markeredgecolor='g')
plt.title('2017-2018各产业季度生产总值折线图')



plt.rcParams['font.sans-serif']='SimHei'
plt.rcParams['axes.unicode_minus']=False
plt.xticks(x,xticks,rotation=75)
plt.yticks(yticks)
plt.legend(['第一季度','总值'],loc=1)
plt.ylabel('生产总值(亿元)',rotation=90,horizontalalignment='right')

plt.show()