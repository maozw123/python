import matplotlib.pyplot as plt
import numpy as np
# 1.创建画布
# figsize=(20,8) 画布尺寸，单位英寸
# dpi ---像素
# 返回画布对象
plt=plt.figure()

# 2.绘画--以简单的折线图为例
# 先构建坐标---(x0,y0) (x1,y1) (x2,y2)
#用数组来构建坐标轴

x=np.arange(1,6)
y=np.array([8,6,10,12,3])
# plot--折线图
plt.plot(x,y)

# 3.图像展示
plt.show()