import numpy as np

# 先简单的创建一个数组
# 可以使用np.array将列表转化为数组
# arr=np.array([1,2,3,4])
# arr=np.array([[1,2,3,4,1],[2,3,4,5,6]])
arr=np.array([[[1,2,3,4],[2,3,4,5]],[[11,21,3,4],[2,3,4,5]]])
print("arr:\n",arr)
print("arr的类型：\n",type(arr))

print("arr的维度ndim：",arr.ndim)
print("arr的形状shape：",arr.shape)
print("arr的大小size：",arr.size)
print("arr的元素的数据类型dtype：",arr.dtype)
print("arr的每一个元素的大小itemsize：",arr.itemsize)
