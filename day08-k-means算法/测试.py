import numpy as np

a1 = np.array([1, 2, 3, 1])  # [1,2]
a2 = np.array([1, 2, 3, 0])  # [1,2]
# 如果不同维度--报错
# sum_ = 0
# for i in range(a1.shape[0]):
#     sum_ += (a1[i] - a2[i]) ** 2
# dist = np.sqrt(sum_)
# print(dist)




# np.power((a1-a2),2) ---求的对应位置差的平方
dist = np.sqrt(np.sum(np.power((a1-a2),2)))

print(dist)


# （x,y）
# (x,y,z)
#(x,y,z,a)
#(x,y,z,a,b)
